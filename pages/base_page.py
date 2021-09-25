from selenium.common.exceptions import NoSuchElementException
from pages.locators import *


class BasePage:
    """Базовые методы

    Это общие методы, применимые для всех станиц"""

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_LINK), 'Login link not found'

    def should_be_logout_link(self):
        assert self.is_element_present(*HeaderLocators.LOGOUT_LINK), 'Logout link not found'
