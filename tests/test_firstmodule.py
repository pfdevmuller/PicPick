import pytest
from .context import picpick
import picpick.firstmodule

def test_that_needs_no_import():
    x = 2
    assert x == 2

def test_that_imports_module_from_main_package():
    first_class = picpick.firstmodule.FirstClass(4)
    assert first_class.square() == 16


class TestClassTryout:
    # Trying out test classes with setup and teardown

    @classmethod
    def setup_class(self):
        print("Setting up for IntegTestTryout")
        self.some_var = "you got me"

    @classmethod
    def teardown_class(self):
        print("Tearing down for IntegTestTryout")

    def test_in_class(self):
        assert self.some_var == "you got me"
