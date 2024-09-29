from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Model(BaseModel):
    model_name: str = Field(..., description="Name of the trained model")
    gridfs_path: str = Field(
        ..., description="Path in GridFS where the model is stored"
    )

    type_model: str = Field(..., description="Name of the trained model")
    accuracy: float = Field(..., description="Accuracy of the model")
    precision: float = Field(..., description="Precision of the model")
    recall: float = Field(..., description="Recall of the model")
    f1_score: float = Field(..., description="F1 score of the model")

    last_trained: Optional[datetime] = Field(
        None, description="Date when the model was last trained"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "RandomForestModel_v1",
                "type_model": "Bitcoin",
                "gridfs_path": "/path/to/model/in/gridfs",
                "accuracy": 0.10,
                "precision": 0.20,
                "recall": 0.30,
                "f1_score": 0.40,
                "last_trained": "2024-09-10T12:00:00",
            }
        }


class ModelUpdate(BaseModel):
    model_name: Optional[str] = Field(None, description="Name of the trained model")
    gridfs_path: Optional[str] = Field(
        None, description="Path in GridFS where the model is stored"
    )
    type_model: Optional[str] = Field(..., description="Name of the trained model")

    accuracy: Optional[float] = Field(None, description="Accuracy of the model")
    precision: Optional[float] = Field(None, description="Precision of the model")
    recall: Optional[float] = Field(None, description="Recall of the model")
    f1_score: Optional[float] = Field(None, description="F1 score of the model")

    last_trained: Optional[datetime] = Field(
        None, description="Date when the model was last trained"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "RandomForestModel_v1",
                "type_model": "Bitcoin",
                "gridfs_path": "/path/to/model/in/gridfs",
                "accuracy": 0.10,
                "precision": 0.20,
                "recall": 0.30,
                "f1_score": 0.40,
                "last_trained": "2024-09-10T12:00:00",
            }
        }
