from pydantic import BaseModel

class PredictionRequest(BaseModel):
    crypto: str
    days: int
    timesteps: int = 30
