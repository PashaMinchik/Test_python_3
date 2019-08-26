
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


from pages.third_page_birth_time import BirthTimePage
from pages.first_page_steam import HomePage
from pages.fourth_page_my_game import Game
from pages.fifth_page_install import Install
from pages.second_page_games import GamesPage
from configure.browser_config import BrowserFactory


class TestSteam:
    driver: WebDriver
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": r"C:\Users\p.minchik\Downloads",
                   "directory_upgrade": True,
                   "safebrowsing.enabled": True,
                   "intl.accept_languages": "en"}
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    @classmethod
    def setup_class(cls):
        cls.home_page: HomePage = HomePage(cls.driver)
        cls.game_page: GamesPage = GamesPage(cls.driver)
        cls.birth_time_page: BirthTimePage = BirthTimePage(cls.driver)
        cls.game: Game = Game(cls.driver)
        cls.download: Install = Install(cls.driver)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


   #@pytest.fixture(scope="module")
   #def start_testing(self):
   #    self.driver = BrowserFactory.start_browser(self, "Chrome")
   #    self.driver.implicitly_wait(10)
   #    self.driver.maximize_window()

   #@pytest.fixture()
   #def setup_test(self):
   #    yield
   #    self.driver.implicitly_wait(3)

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

    def test_9(self):
        self.download.click_install_again()
        self.download.check_file_and_close_page()

    @classmethod
    def teardown_class(cls):
       cls.driver.close()
