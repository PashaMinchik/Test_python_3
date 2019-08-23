import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from pages.games_page import GamesPage
from pages.birth_time_page import BirthTimePage
from pages.steam_page import HomePage
from pages.my_game import Game
from pages.install_page import Install


class TestSteam:
    # driver = BrowserFactory.driver
    driver: WebDriver
    chrome_options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": r"C:\Users\p.minchik\Downloads",
                   "directory_upgrade": True,
                   "safebrowsing.enabled": True}
    chrome_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    @classmethod
    def setup_class(cls):
        #cls.driver = WebDriver
        #cls.chrome_options = webdriver.ChromeOptions()
        #cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=cls.chrome_options)
        cls.home_page: HomePage = HomePage(cls.driver)
        cls.game_page: GamesPage = GamesPage(cls.driver)
        cls.birth_time_page: BirthTimePage = BirthTimePage(cls.driver)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.game: Game = Game(cls.driver)
        cls.download: Install = Install(cls.driver)
        cls.preferences = {"download.default_directory": r"C:\Users\p.minchik\Downloads",
                           "directory_upgrade": True,
                           "safebrowsing.enabled": True}

    @pytest.fixture()
    def setup_test(self):
        yield
        self.driver.implicitly_wait(3)

    def test_1(self):
        self.home_page.get_home_page()

    def test_2(self):
        self.home_page.click_actions()

    def test_3(self):
        self.game_page.click_top_sellers()

    def test_4(self):
        self.game_page.get_max_discount()

    def test_5(self):
        self.game_page.get_info_game()

    def test_6(self):
        self.game_page.choose_max_discount()

    def test_7(self):
        self.birth_time_page.choose_birth_time()

    def test_8(self):
        self.game.get_info_game1()
        assert self.game_page, self.game
        self.game.click_install()
        self.chrome_options.add_experimental_option("prefs", self.preferences)

    def test_9(self):
        self.download.click_install_again()
        self.driver.implicitly_wait(5)

# @classmethod
# def teardown_class(cls):
#    #cls.driver.close()
