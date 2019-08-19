from selenium import webdriver
import time
import unittest
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.steam_page import HomePage
from pages.actions_page import ActionsPage
from locators.locators import Locators


class TestSteam:
    driver: WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    home_page: HomePage = HomePage(driver)
    action_page: ActionsPage = ActionsPage(driver)

    @classmethod
    def setup_class(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1(self):
        self.home_page.get_home_page()

    def test_2(self):
        self.home_page.click_actions()

    def test_3(self):
        self.action_page.click_top_sellers()

    def test_4(self):
        self.action_page.choose_sellers()

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        cls.driver.close()
