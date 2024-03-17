from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")

    def verify_url(self):
        assert "magento.softwaretestingboard.com/catalogsearch/result/?q=" in self.driver.current_url

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

