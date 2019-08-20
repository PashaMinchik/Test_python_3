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


class Test2Steam:
    driver: WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    home_page: HomePage = HomePage(driver)
    action_page: ActionsPage = ActionsPage(driver)

    driver.get("https://store.steampowered.com/tags/ru/%D0%AD%D0%BA%D1%88%D0%B5%D0%BD/#p=0&tab=TopSellers")
    all_trails = []
    sale = driver.find_elements_by_xpath(
        "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%')]")
    print(sale)
    for link in sale:
        all_trails.append(link.get_attribute("innerText"))

    print(all_trails)
    max_discount = max(all_trails)
    print(max_discount)
    driver.find_element_by_xpath(
        "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%s')]" % max_discount).click()

    #for j in all_trails:
    #    if j == '%':
    #        all_trails.remove('%')

