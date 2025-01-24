import allure
import pytest
from assertpy import assert_that
from tests.test_base import BaseTest
from pages.search_product import search_Page


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("login")
@allure.story("login Feature Functionality")
class Testsearch(BaseTest):
    @allure.description("login test")
    @allure.title("login Test")
    @pytest.mark.run()
    def test_valid_search(self):
        searchpage = search_Page(self.driver)
        searchpage.click_search_bar()
        searchpage.wait_until_page_loaded()
        searchpage.most_visit_for_search()
        searchpage.wait_until_page_loaded()
        searchpage.dropDown_select("samsung a12")
        searchpage.wait_until_page_loaded()
        searchpage.dropdown_select_item()



