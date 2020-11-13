from abc import ABC

from python_project.test_logger import TestLogger


class PyTest(ABC):
    def __init__(self, logger: TestLogger, expression):
        self.tester_logger = logger
        self.expression = expression
