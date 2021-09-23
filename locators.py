from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '.kabinet-icon-adaptiv')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logoutForm')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#loginForm')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[class="col-md-7"] [name="Email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[class="col-md-7"] [name="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="col-md-offset-3 col-md-9"] [class="btn btn-success"]')