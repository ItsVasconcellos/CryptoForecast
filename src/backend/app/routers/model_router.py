from fastapi import APIRouter, HTTPException
from typing import List
from app.utils.PredictionRequest import PredictionRequest
from app.models.result import Result
from app.services.grid_service import GridServiceSingleton
from app.services.model_service import ModelServiceSingleton
from app.utils.crypto import Crypto, Models_Crypto
import logging
import datetime as dt

router = APIRouter(prefix="/api/model", tags=["Model"])

# Get the logger
logger = logging.getLogger("fastapi")


@router.get(
    "/train",
    response_model=str,
    response_description="Train all models",
)
async def train_models():
    GridServiceSingleton.get_instance().train_models()
    return "All models trained successfully"


@router.post(
    "/predict",
    response_model=list[Result],
    response_description="Make predictions",
)
async def make_prediction(request: PredictionRequest):
    try:

        predictions = GridServiceSingleton.get_instance().predict(
            request.crypto, request.days, time_steps=request.timesteps
        )
        results = []
        for prediction in predictions:
            result = Result(date=prediction["date"], value=prediction["price"])
            results.append(result)
        return results

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
