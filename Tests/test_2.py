from selenium import webdriver
import time
import unittest
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from pages.steam_page import HomePage
from locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from pages.birth_time_page import BirthTimePage
from pages.games_page import GamesPage


import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.games_page import GamesPage
from pages.birth_time_page import BirthTimePage
from pages.steam_page import HomePage
from pages.my_game import Game


def get_info_game():
    pass


class Game2(GamesPage):
    def __init__(self, driver):
        super().__init__(driver)
    # driver = BrowserFactory.driver
    driver: WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        driver.get("https://store.steampowered.com/bundle/5433/Mafia_Triple_Pack/")
        print(get_info_game())
