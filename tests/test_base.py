import pytest
from tests.conftest import  create_driver



from utils.json_parser import JsonParser


class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, pages, create_driver):
        self.pages = pages
        self.driver = create_driver
