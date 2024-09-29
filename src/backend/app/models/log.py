from datetime import datetime
from pydantic import BaseModel
    

class LogModel(BaseModel):
    log_level: str
    message: str
    timestamp: datetime = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.now()

    class Config:
        arbitrary_types_allowed = True
