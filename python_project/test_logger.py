import logging
from abc import ABC
from typing import Optional


class TestLogger(ABC):
    def __init__(self, logging_name: Optional[str]):
        logging_name = logging_name if not None else "testing"
        self.logger = logging.getLogger(logging_name)

    def _success_writer(self):
        raise NotImplemented

    def _failure_writer(self):
        raise NotImplemented

    def conditional_logger_writer(self, condition: bool):
        if condition:
            return self._success_writer()
        else:
            return self._failure_writer()
