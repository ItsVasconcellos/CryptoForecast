from datetime import datetime
from pydantic import BaseModel, Field


class Result(BaseModel):
    date: datetime = Field(..., description="Date of the prediction")
    value: float = Field(..., description="Predicted value")

    class Config:
        json_schema_extra = {"example": {"VALUE": 200, "DATA": "2023-10-01T12:00:00Z"}}
