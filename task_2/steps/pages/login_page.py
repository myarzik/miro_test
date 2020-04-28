from .base_page import BasePage
from .locators import LOGIN_PAGE_LOCATORS


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators_dictionary.update(LOGIN_PAGE_LOCATORS)
