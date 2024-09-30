from app.utils.crypto import Crypto
from app.services.model_service import ModelService
from app.services.create_model import train_models, get_data
from app.repositories.grid_repo import GridFSRepository
import pandas as pd
import numpy as np
from typing import Optional
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import io
import tempfile
import os
from tensorflow.keras.models import load_model


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
            with open(model_data, "rb") as model_file:
                model_bytes = model_file.read()
            file_id = self.gridfs_repo.save_model(f"{crypto}.h5", model_bytes)
            file_ids.append(file_id)
        return file_ids

    def load_model_from_local(self, model_name: str):
        try:
            # Construct the path to the model file
            model_path = os.path.join(os.path.dirname(__file__), "../modelos", model_name)

            # Load the model from the specified path
            model = load_model(model_path)

            return model
        except Exception as e:
            print(f"An error occurred while loading the model from local path: {e}")
            return None

    def delete_model(self, file_id: str):
        self.gridfs_repo.delete_model(file_id)

    def predict(
        self,  crypto: str, datetime: datetime, time_steps=30
    ) -> list[dict]:
        future_dates = pd.date_range(start=datetime, periods=30)
        data = get_data(crypto)
        close_prices = data["Close"].values

        last_prices = close_prices[-time_steps:]

        scaler = MinMaxScaler(feature_range=(0, 1))
        last_prices_scaled = scaler.fit_transform(last_prices.reshape(-1, 1))

        predicted_prices = []

        model = self.load_model_from_local(f"{crypto}.h5")

        for i in range(len(future_dates)):
            x_pred = np.array([last_prices_scaled[-time_steps:, 0]])
            x_pred = np.reshape(x_pred, (x_pred.shape[0], x_pred.shape[1], 1))
            predicted_price_scaled = model.predict(x_pred)
            predicted_price = scaler.inverse_transform(predicted_price_scaled)
            predicted_prices.append(predicted_price.flatten()[0])
            next_input_scaled = np.zeros_like(last_prices_scaled[-1])
            next_input_scaled[0] = predicted_price_scaled[0]
            last_prices_scaled = np.vstack([last_prices_scaled, next_input_scaled])
        future_data = [
            {"Date": date, "Predicted Price": price}
            for date, price in zip(future_dates, predicted_prices)
        ]
        return future_data


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
