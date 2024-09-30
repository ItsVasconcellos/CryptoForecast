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

    def to_dict(self):
        return {
            "log_level": self.log_level,
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
        }

    class Config:
        arbitrary_types_allowed = True
