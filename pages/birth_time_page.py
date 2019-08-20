from locators.locators import Locators
from selenium.webdriver.support.ui import Select


class BirthTimePage:

    def __init__(self, driver):
        self.driver = driver
        self.age_choose = Locators.age_choose

    def choose_birth_time(self) -> object:
        x = self.driver.find_element_by_id(self.age_choose)
        x.click()
        Select(x.select_by_visible_text("2000"))