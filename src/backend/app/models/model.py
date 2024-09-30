from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Model(BaseModel):
    model_name: str = Field(..., description="Name of the trained model")
    gridfs_path: str = Field(
        ..., description="Path in GridFS where the model is stored"
    )
    last_trained: Optional[datetime] = Field(
        None, description="Date when the model was last trained"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "BitcoinPriceModel_v1",
                "gridfs_path": "/path/to/model/in/gridfs",
                "last_trained": "2024-09-10T12:00:00",
            }
        }


class ModelUpdate(BaseModel):
    model_name: Optional[str] = Field(None, description="Name of the trained model")
    gridfs_path: Optional[str] = Field(
        None, description="Path in GridFS where the model is stored"
    )

    last_trained: Optional[datetime] = Field(
        None, description="Date when the model was last trained"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "BitcoinPriceModel_v1",
                "gridfs_path": "/path/to/model/in/gridfs",
                "last_trained": "2024-09-10T12:00:00",
            }
        }
