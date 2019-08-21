from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    driver: WebDriver

    def start_browser(self, browser_name):
        if browser_name == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        return self.driver
