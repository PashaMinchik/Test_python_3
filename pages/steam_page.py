import time

from locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.action: ActionChains = ActionChains(driver)
        self.home_site = "https://store.steampowered.com/"
        self.actions_click = Locators.actions_click
        self.move_to_games = Locators.move_to_games

    def get_home_page(self) -> object:
        self.driver.get(self.home_site)

    def click_actions(self) -> object:
        self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.actions_click).click()
