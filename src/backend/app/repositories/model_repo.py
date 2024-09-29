from datetime import datetime
from typing import Optional

from app.db.mongodb import MongoDB
from app.models.model import Model, ModelUpdate


class ModelRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection_model = db.get_collection("model")

    def get_all_models(self) -> list[Model]:
        documents = self.collection.find()
        return [Model(**document) for document in documents]

    def get_model(self, model_name: str) -> Optional[Model]:
        document = self.collection.find_one({"model_name": model_name})
        return Model(**document) if document else None

    def save_model(self, model: Model):
        self.collection.insert_one(model.model_dump(by_alias=True))
        return model.model_name

    def update_model(self, model_name: str, model: ModelUpdate | Model) -> bool:
        result = self.collection.update_one(
            {"model_name": model_name},
            {"$set": model.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0
