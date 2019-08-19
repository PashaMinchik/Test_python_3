from locators.locators import Locators


class ActionsPage:

    def __init__(self, driver):
        self.driver = driver
        self.top_sellers = Locators.top_sellers
        self.choose_sellers = Locators.choose_sellers

    def click_top_sellers(self) -> object:
        self.driver.find_element_by_xpath(self.top_sellers).click()

    def max_discount(self):
        print(len(self.driver.find_element_by_xpath(self.choose_sellers)))
