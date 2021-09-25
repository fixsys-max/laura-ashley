from pages.base_page import BasePage
from pages.locators import *


class RegistrationPage(BasePage):
    """Методы странцы регистрации"""
    def should_be_warning_message(self):
        assert self.is_element_present(*LoginPageLocators.WARNING_MESSAGE), 'Warning message not found'

    def fill_out_registration_form(self, **kwargs):
        data = kwargs
        self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(data['case']['mail'])
        self.browser.find_element(*RegistrationPageLocators.PHONE_FIELD).send_keys(data['case']['phone'])
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(data['case']['password'])
        self.browser.find_element(*RegistrationPageLocators.CONFIRM_FIELD).send_keys(data['case']['confirm'])
        self.browser.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(data['case']['first_name'])
        self.browser.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(data['case']['last_name'])
        self.browser.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()




