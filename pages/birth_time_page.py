from selenium.webdriver.support.select import Select

from locators.locators import Locators
from selenium.webdriver.support.ui import Select


class BirthTimePage:

    def __init__(self, driver):
        self.driver = driver
        self.age_choose = Locators.age_choose
        self.select = Select

    def choose_birth_time(self) -> object:
        self.select = Select(self.driver.find_element_by_id(self.age_choose))
        self.select.select_by_visible_text("1995")