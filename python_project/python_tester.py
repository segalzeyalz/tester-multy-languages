from python_project.py_jest import PyJest
from python_project.test_logger import TestLogger


class PythonJestLogger(TestLogger):
    def describe(self, description, fn):
        self.logger.info(description)
        fn()

    def it(self, msg, fn):
        self.describe(f'{msg}', fn)

    def _success_writer(self):
        self.logger.info("pass")
        return True

    def _failure_writer(self):
        self.logger.error("fail")
        return False


tester_logger = PythonJestLogger("jest_test")


def expect(exp):
    return PyJest(tester_logger, exp)
