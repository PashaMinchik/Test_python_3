import time
import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://store.steampowered.com/agecheck/sub/88802")
driver.find_element_by_xpath("//div[@class='main_content_ctn']//a[@class='btnv6_blue_hoverfade btn_medium']//span[1]").click()
