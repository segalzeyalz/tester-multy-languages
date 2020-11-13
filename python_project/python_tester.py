from python_project.py_jest import PyJest
from python_project.test_logger import TestLogger


class PythonJestLogger(TestLogger):
    def write(self, msg: str):
        self.logger.info(msg)

    def _success_writer(self):
        self.write("pass")
        return True

    def _failure_writer(self):
        self.logger.error("fail")
        return False


tester_logger = PythonJestLogger("jest_test")


def expect(exp):
    return PyJest(tester_logger, exp)


def describe(description, fn):
    tester_logger.write(description)
    fn()


def it(msg, fn):
    describe(f'{msg}', fn)
