from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".action.search")
    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        self.find(self.BUTTON_SEARCH).click()

    def find_all(self, locator):
        return self.driver.find_elements(*locator)


