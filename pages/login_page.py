import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """ service  login  Page """

    profile_icon = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div/div[2]/a/button/div")
    input_mobile = (By.XPATH, "//input[contains(@class,'px-2 TextField_TextField__input__hFMFl')]")
    enter_button = (By.XPATH, "//div[text()='ورود']")
    enter_password = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//div[text()='تایید']")
    confirm_login = (By.XPATH, "//img[@alt='لوگوی دیجیکالا']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on profile icon")
    def click_profile_icon(self):
        self.click(self.profile_icon)

    @allure.step("Enter mobile")
    def enter_fullname(self, username):
        self.click(self.input_mobile)
        self.fill_text(self.input_mobile, username)

    @allure.step("Click Next")
    def click_next(self):
        self.scroll_to_bottom()
        self.click(self.enter_button)

    @allure.step("enter password")
    def enter_passcode(self, password):
        self.fill_text(self.enter_password, password)

    @allure.step("click confirm password")
    def click_confirm_button(self):
        self.click(self.login_button)

    @allure.step("Get success message and see profile")
    def successful_login(self):
        self.wait_until_page_loaded()
        return self.get_text(self.confirm_login)

    @allure.step("take screenshot")
    def capture_login_modele(self):
        """ capture configuration login """
        self.save_confirmation_model(self.confirm_login)
