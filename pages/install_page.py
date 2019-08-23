from locators.locators import Locators
from pages.my_game import Game
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Install(Game):
    def __init__(self, driver: object):
        super().__init__(driver)
        self.stem_install_click = Locators.stem_install_click
        self.options = Options()

    def click_install_again(self):
        self.driver.find_element_by_xpath(self.stem_install_click).click()

# def click_save(self):
#    preferences = {"download.default_directory": r"C:\Users\p.minchik\Downloads",
#                   "directory_upgrade": True,
#                   "safebrowsing.enabled": True}
#    self.chrome_options.add_experimental_option("prefs", preferences)
