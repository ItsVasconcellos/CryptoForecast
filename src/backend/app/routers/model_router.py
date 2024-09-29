from fastapi import APIRouter, HTTPException
from typing import List
from app.models.model import ModelUpdate
from app.models.result import Result
from app.services.grid_service import GridServiceSingleton
from app.services.model_service import ModelServiceSingleton
from app.utils.crypto import Crypto
import logging

router = APIRouter(prefix="/api/model", tags=["Logs"])

# Get the logger
logger = logging.getLogger("fastapi")


@router.get(
    "/train",
    response_model=str,
    response_description="Train all models",
)
async def train_models():
    files_ids = GridServiceSingleton.get_instance().train_models()
    for i, file_id in enumerate(files_ids):
        ModelServiceSingleton.get_instance().update_model(
            Crypto[i], ModelUpdate(gridfs_path=file_id)
        )
    return "All models trained successfully"


@router.post("/predict/{crypto}", response_model=list[Result])
async def make_prediction(crypto: str, prediction_request: PredictionRequest):
    grid_path = ModelServiceSingleton.get_instance().get_model(crypto)
    model = GridServiceSingleton.get_instance().get_model(grid_path)

    try:
        predictions = model.predict([prediction_request.input_data])

        return {"predictions": predictions.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
