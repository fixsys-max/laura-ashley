from pages.base_page import BasePage
from pages.locators import *


class LoginPage(BasePage):
    """Методы страницы логина"""
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_warning_message(self):
        assert self.is_element_present(*LoginPageLocators.WARNING_MESSAGE), 'Warning message not found'

    def fill_out_login_form(self, **kwargs):
        case = kwargs
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(case['mail'])
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(case['password'])
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
