from python_project.py_test import PyTest


class PyJest(PyTest):
    def to_be(self, assertion: bool):
        is_equal = self.expression == assertion
        return self.tester_logger.conditional_logger_writer(is_equal)
