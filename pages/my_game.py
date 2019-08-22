from pages.games_page import GamesPage
from locators.locators import Locators


class Game:
    def __init__(self, driver):
        self.x = str
        self.game_info1 = str
        self.driver = driver
        self.game1_prise = Locators.game1_prise
        self.game1_discount = Locators.game1_discount
        self.game1_base_discount = Locators.game1_base_discount

    def get_info_game1(self) -> object:
        self.game_info1 = self.driver.find_element_by_xpath(self.game1_discount).get_attribute("innerText")
        self.x = self.driver.find_element_by_xpath(self.game1_base_discount).get_attribute("innerText")
        #self.game_info1.append(self.driver.find_element_by_xpath(self.game1_prise).get_attribute("innerText"))
        print(self.game_info1)
        print(self.x)
        print(self.game_info1 - self.x)
