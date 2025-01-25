import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure

from pages.base_page import BasePage


class search_Page(BasePage):
    search_icon = (By.XPATH, "//div[contains(@class,'lg:text-body-2 text-button-1')]")
    most_visit = (By.XPATH, "(//span[@data-cro-id='plp-sort'])[2]")
    selected_item = (By.XPATH, "//div[@class='grow text-right']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on search bar")
    def click_search_bar(self):
        self.click(self.search_icon)
        self.fill_text(self.search_icon, "iphon")

    @allure.step("select most visit")
    def most_visit_for_search(self):
        self.wait_until_page_loaded()
        self.click(self.most_visit)


    @allure.step("select item category")
    def dropdown_select_item(self):
        self.wait_until_page_loaded()
        self.dropDown_select(self.selected_item)




