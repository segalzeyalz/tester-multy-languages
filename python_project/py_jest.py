from python_project.test_logger import TestLogger


class PyJest:
    def __init__(self, logger: TestLogger, expression):
        self.tester_logger = logger
        self.expression = expression

    def to_be(self, assertion: bool):
        is_equal = self.expression == assertion
        return self.tester_logger.conditional_logger_writer(is_equal)

