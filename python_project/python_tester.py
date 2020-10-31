import logging


class PythonJestLogger:
    def __init__(self):
        self.logger = logging.getLogger("python_jest")

    def describe(self, description, fn):
        # self.logger.info(description)
        print(description)
        fn()

    def it(self, msg, fn):
        self.describe(f'{msg}', fn)

    def _success_writer(self):
        print("pass")
        self.logger.info("pass")
        return True

    def _failure_writer(self):
        print("fail")
        # self.logger.error("fail")
        return False

    def conditional_logger_writer(self, condition: bool):
        if condition:
            return self._success_writer()
        else:
            return self._failure_writer()


tester_logger = PythonJestLogger()


def matchers(exp):
    return {
        "to_be": lambda assertion: tester_logger.conditional_logger_writer(exp == assertion)
    }


def expect(exp):
    return matchers(exp)


expect(5)["to_be"](5)
