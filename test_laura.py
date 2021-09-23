from selenium.common.exceptions import NoSuchElementException
from locators import *

main_page_link = 'https://laura-ashley.com.ua/'
login_page_link = 'https://laura-ashley.com.ua/Account/Login/'


def test_login_link_is_present(browser):
    browser.get(main_page_link)
    browser.implicitly_wait(3)
    try:
        login_link = browser.find_element(*HeaderLocators.LOGIN_LINK)
    except NoSuchElementException:
        login_link = False
    assert login_link, 'Login link not found'


def test_guest_can_go_to_login_page(browser):
    browser.get(main_page_link)
    browser.implicitly_wait(3)
    try:
        browser.find_element(*HeaderLocators.LOGIN_LINK).click()
        login_form = browser.find_element(*LoginPageLocators.LOGIN_FORM)
    except NoSuchElementException:
        login_form = False
    assert login_form, 'Login form or login link not found'


def test_guest_can_login(browser):
    browser.get(login_page_link)
    browser.implicitly_wait(3)
    try:
        browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('mail@mail.com')
        browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('1234')
        browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        logout_link = browser.find_element(*HeaderLocators.LOGOUT_LINK)
    except NoSuchElementException:
        logout_link = False
    assert logout_link, 'Logout link not found'
