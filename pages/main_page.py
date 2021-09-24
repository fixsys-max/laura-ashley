# from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import *


class MainPage(BasePage):
    def gp_to_login_page(self):
        login_link = self.browser.find_element(*HeaderLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_LINK), 'Login link not found'

    def should_be_logout_link(self):
        assert self.is_element_present(*HeaderLocators.LOGOUT_LINK), 'Logout link not found'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'
