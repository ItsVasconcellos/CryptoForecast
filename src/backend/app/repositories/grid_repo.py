import gridfs
from app.db.mongodb import MongoDB
from bson.objectid import ObjectId


class GridFSRepository:
    def __init__(self, db: MongoDB):
        self.fs = gridfs.GridFS(db.get_database())

    def save_model(self, filename: str, model_data: bytes) -> str:
        file_id = self.fs.put(model_data, filename=filename)
        return str(file_id)

    def get_model(self, file_id: str) -> bytes:
        grid_out = self.fs.get(ObjectId(file_id))
        return grid_out.read()

    def delete_model(self, file_id: str):
        self.fs.delete(ObjectId(file_id))
