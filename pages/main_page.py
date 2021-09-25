from pages.base_page import BasePage
from pages.locators import *


class MainPage(BasePage):
    """Методы домашней (основной) страницы"""
    def gp_to_login_page(self):
        login_link = self.browser.find_element(*HeaderLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'
