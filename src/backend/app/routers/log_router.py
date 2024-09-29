from fastapi import APIRouter, HTTPException
from typing import List
from app.models.log import LogModel
from app.services.log_service import LogServiceSingleton
import logging

router = APIRouter(prefix="/api/logs", tags=["Logs"])

# Get the logger
logger = logging.getLogger("fastapi")


@router.get(
    "/",
    response_model=list[LogModel],
    response_description="List of the quantity of each possible failure codes was predicted by month",
)
def get_logs(limit: int = 100):
    logs = LogServiceSingleton.get_instance().get_logs(limit)
    return logs
