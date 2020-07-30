import pytest
from app import app


class BasicTestCase:
    def test_index(self):
        tester = app.test
