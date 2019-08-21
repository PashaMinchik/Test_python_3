from selenium import webdriver
import time
import unittest
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from pages.steam_page import HomePage
from pages.actions_page import ActionsPage
from locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from pages.birth_time_page import BirthTimePage


class Test2Steam:
    driver: WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    home_page: HomePage = HomePage(driver)
    action_page: ActionsPage = ActionsPage(driver)
    select = Select
    age_choose = Locators.age_choose

    driver.get("https://store.steampowered.com/tags/ru/Экшен/#p=0&tab=TopSellers")
    try:
        select = Select(driver.find_element_by_id(age_choose))
        select.select_by_visible_text("1995")
        driver.find_element_by_xpath("//a[@class='btnv6_blue_hoverfade btn_medium']").click()
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//span[text()='Открыть страницу']").click()
        except NoSuchElementException:
            pass





