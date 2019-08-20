from locators.locators import Locators


class ActionsPage:

    def __init__(self, driver):
        self.driver = driver
        self.top_sellers = Locators.top_sellers
        self.choose_discounts = Locators.choose_discounts
        self.all_trails = []
        self.click_max_discount = Locators.click_max_discount

    def click_top_sellers(self) -> object:
        self.driver.find_element_by_xpath(self.top_sellers).click()

    def max_discount(self):
        #self.sale = self.driver.find_elements_by_xpath(self.choose_discounts)
        print(self.driver.find_elements_by_xpath(self.choose_discounts))
        for link in self.driver.find_elements_by_xpath(self.choose_discounts):
            self.all_trails.append(link.get_attribute("innerText"))

        print(self.all_trails)
        max_discount = max(self.all_trails)
        print(max_discount)
        self.driver.find_element_by_xpath(self.click_max_discount % max_discount).click()
