from datetime import datetime
from typing import Optional

from app.db.mongodb import MongoDB
from app.models.log import LogModel


class LogRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection = db.get_collection("logs")

    def save_log(self, log: LogModel):
        self.collection.insert_one(log.to_dict())

    def get_logs(self, limit: int = 100):
        logs = self.collection.find().sort("timestamp", -1).limit(limit)
        return [LogModel(**{k: v for k, v in log.items() if k != '_id'}) for log in logs]
