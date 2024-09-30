from fastapi import APIRouter, HTTPException
from typing import List
from app.utils.PredictionRequest import PredictionRequest
from app.models.result import Result
from app.services.grid_service import GridServiceSingleton
from app.services.log_service import LogServiceSingleton
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
    try:
        GridServiceSingleton.get_instance().train_models()
        LogServiceSingleton.get_instance().emit(
            logging.LogRecord(
                "fastapi",
                logging.INFO,
                dt.datetime.now(),
                msg="/api/models/train was executed with  success",
                lineno=None,
                exc_info=None,
                args=None,
            )
        )
        return "All models trained successfully"
    except Exception as e:
        LogServiceSingleton.get_instance().emit(
            logging.LogRecord(
                "fastapi",
                logging.ERROR,
                dt.datetime.now(),
                msg="An error occurred while executing /api/models/train",
                lineno=None,
                exc_info=None,
                args=None,
            )
        )
        raise HTTPException(status_code=500, detail=str(e))


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
        LogServiceSingleton.get_instance().emit(
            logging.LogRecord(
                "fastapi",
                logging.INFO,
                dt.datetime.now(),
                msg="/api/models/predictions executed with sucecess",
                lineno=None,
                exc_info=None,
                args=None,
            )
        )
        return results

    except Exception as e:
        print(e)
        LogServiceSingleton.get_instance().emit(
            logging.LogRecord(
                "fastapi",
                logging.ERROR,
                dt.datetime.now(),
                msg="An error occurred while exectuing /api/models/predictions",
                lineno=None,
                exc_info=None,
                args=None,
            )
        )
        raise HTTPException(status_code=500, detail=str(e))
