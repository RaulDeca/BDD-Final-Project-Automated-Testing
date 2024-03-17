from pages.base_page import BasePage


class PrivacyPage(BasePage):

    PRIVACY_PAGE_URL = "https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode#privacy-policy-title-1"


    def open(self):
        self.driver.get(self.PRIVACY_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.PRIVACY_PAGE_URL