from selenium.webdriver.common.by import By
"""Файл для хранения локаторов

Набор локаторов (селекторов), применяемых на страницах сайта"""


class HeaderLocators:
    """Локаторы хэдера"""
    LOGIN_LINK = (By.CSS_SELECTOR, '.kabinet-icon-adaptiv')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logoutForm')


class LoginPageLocators:
    """Локаторы страницы логина"""
    LOGIN_FORM = (By.CSS_SELECTOR, '#loginForm')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[class="col-md-7"] [name="Email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[class="col-md-7"] [name="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="col-md-offset-3 col-md-9"] [class="btn btn-success"]')
    WARNING_MESSAGE = (By.CSS_SELECTOR, '.validation-summary-errors')


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    EMAIL_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="Email"]')
    PHONE_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="PhoneNumber"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="Password"]')
    CONFIRM_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="ConfirmPassword"]')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="FirstName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[class="col-md-4"] [name="LastName"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[class="col-md-offset-1 col-md-10 text-center"] [class="btn btn-success"]')
    WARNING_MESSAGE = (By.CSS_SELECTOR, '.validation-summary-errors')
