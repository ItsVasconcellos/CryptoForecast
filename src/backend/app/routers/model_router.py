from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from app.models.model import ModelUpdate
from app.models.result import Result
from app.services.grid_service import GridServiceSingleton
from app.services.model_service import ModelServiceSingleton
from app.utils.crypto import Crypto, Models_Crypto
import logging

router = APIRouter(prefix="/api/model", tags=["Model"])

# Get the logger
logger = logging.getLogger("fastapi")


@router.get(
    "/train",
    response_model=str,
    response_description="Train all models",
)
async def train_models():
    models_exists = ModelServiceSingleton.get_instance().get_all_models()
    if len(models_exists) != len(Crypto):
        for model in Models_Crypto:
            ModelServiceSingleton.get_instance().create_model(model)
    files_ids = GridServiceSingleton.get_instance().train_models()
    print(files_ids)
    for i, file_id in enumerate(files_ids):
        ModelServiceSingleton.get_instance().update_model(
            Crypto[i], ModelUpdate(gridfs_path=file_id)
        )
    return "All models trained successfully"


@router.post(
    "/predict/{crypto}",
    response_model=list[Result],
    response_description="Make predictions",
)
async def make_prediction(
    crypto: str, prediction_request: datetime, timesteps: int = 30
):
    try:
        

        predictions = GridServiceSingleton.get_instance().predict(
             crypto, prediction_request, time_steps=timesteps
        )
        results = []
        for i, prediction in enumerate(predictions):
            result = Result(prediction=prediction, timestamp=prediction_request[i])
            results.append(result)
        return results

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
