from pages.base_page import BasePage
from pages.locators import *


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_login_link(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_LINK), 'Login link not found'

    def should_be_logout_link(self):
        assert self.is_element_present(*HeaderLocators.LOGOUT_LINK), 'Logout link not found'

    def fill_out_login_form(self, mail, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(mail)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
