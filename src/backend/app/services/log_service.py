from typing import Optional
import logging
from app.repositories.log_repo import LogRepository
from app.models.log import LogModel


class LogService(logging.Handler):
    def __init__(self, logRepo: LogRepository):
        super().__init__()
        self.repository = logRepo

    def emit(self, record):
        log_message = self.format(record)
        log_model = LogModel(log_level=record.levelname, message=log_message)
        self.repository.save_log(log_model)

    def get_logs(self, limit: int = 100) -> list[LogModel]:
        return self.repository.get_logs(limit)


class LogServiceSingleton:
    __instance: Optional[LogService] = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @staticmethod
    def initialize(log_repo: LogRepository):
        LogServiceSingleton.__instance = LogService(log_repo)

    @staticmethod
    def get_instance() -> LogService:
        if LogServiceSingleton.__instance is None:
            raise RuntimeError("LogServiceSingleton not initiated yet")

        return LogServiceSingleton.__instance


def setup_logging(logRepo: LogRepository):
    log_service = LogService(logRepo)
    log_service.setLevel(logging.INFO)

    formatter = logging.Formatter("%(message)s")
    log_service.setFormatter(formatter)

    logger = logging.getLogger("fastapi")
    logger.setLevel(logging.INFO)
    logger.addHandler(log_service)
    return logger
