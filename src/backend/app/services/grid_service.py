from app.services.model_service import ModelService
from app.services.create_model import train_models
from app.repositories.grid_repo import GridFSRepository
from typing import Optional
import pickle
from app.utils.crypto import Crypto


class GridService:
    def __init__(self, gridfs_repo: GridFSRepository):
        self.gridfs_repo = gridfs_repo

    def save_model(self, filename: str, model_data: bytes) -> str:
        return self.gridfs_repo.save_model(filename, model_data)

    def get_model(self, file_id: str) -> bytes:
        return self.gridfs_repo.get_model(file_id)

    def train_models(self):
        file_ids = []
        for crypto in Crypto:
            model_data = train_models(crypto)
            file_id = self.gridfs_repo.save_model(f"{crypto.name}.pkl", model_data)
            file_ids.append(file_id)
        return file_ids

    def get_model(self, file_id: str) -> bytes:
        return self.gridfs_repo.get_model(file_id)

    def load_model(self, file_id: str):
        model_data = self.gridfs_repo.get_model(file_id)
        model = pickle.loads(model_data)  # Assuming the model is serialized with pickle
        return model

    def delete_model(self, file_id: str):

        self.gridfs_repo.delete_model(file_id)


class GridServiceSingleton:
    __instance: Optional[GridService] = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @staticmethod
    def initialize(gridfs_repo: GridFSRepository):
        GridServiceSingleton.__instance = GridService(gridfs_repo)

    @staticmethod
    def get_instance() -> GridService:
        if GridServiceSingleton.__instance is None:
            raise RuntimeError("GridServiceSingleton not initiated yet")
        return GridServiceSingleton.__instance
