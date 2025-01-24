import allure
import pytest
from assertpy import assert_that
from tests.test_base import BaseTest
from pages.login_page import LoginPage
from utils.config_parser import ConfigParserIni


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("login")
@allure.story("login Feature Functionality")
class TestLogin(BaseTest):

    @allure.description("login test")
    @allure.title("login Test")
    @pytest.mark.run()
    def test_valid_login(self):
        config_parser = ConfigParserIni("props.ini")

        username = config_parser.config_section_dict("AUT").get("username")
        print(username)
        password = config_parser.config_section_dict("AUT").get("password")
        print(password)

        loginpage = LoginPage(self.driver)
        loginpage.wait_until_page_loaded()
        loginpage.click_profile_icon()
        loginpage.wait_until_page_loaded()
        loginpage.enter_fullname(username)
        loginpage.click_next()
        loginpage.wait_until_page_loaded()

        loginpage.enter_passcode(password)

        loginpage.click_confirm_button()
        loginpage.wait_until_page_loaded()
        loginpage.capture_login_modele()
        # expected_success_message = self.json_reader.read_from_json()["login"]["success_message"]
        # assert_that(expected_success_message).is_equal_to(success_message)
