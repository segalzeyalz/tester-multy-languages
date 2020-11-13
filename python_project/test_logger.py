import logging
from abc import ABC
from typing import Optional


class TestLogger(ABC):
    def __init__(self, logging_name: Optional[str]):
        logging_name = logging_name if not None else "testing"
        self.logger = logging.getLogger(logging_name)

    def write(self, msg):
        raise NotImplemented

    def _success_writer(self) -> True:
        raise NotImplemented

    def _failure_writer(self) -> False:
        raise NotImplemented

    def conditional_logger_writer(self, condition: bool) -> bool:
        if condition:
            return self._success_writer()
        else:
            return self._failure_writer()
