import pytest
from pages.locators import *
from pages.main_page import MainPage
from pages.login_page import LoginPage

main_page_link = 'https://laura-ashley.com.ua/'
login_page_link = 'https://laura-ashley.com.ua/Account/Login/'


def test_login_link_is_present(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.gp_to_login_page()
    page.should_be_login_form()


def test_guest_can_login(browser):
    mail = 'mail@mail.com'
    password = '1234'
    page = LoginPage(browser, login_page_link)
    page.open()
    page.fill_out_login_form(mail, password)
    page.should_be_logout_link()


def test_login_error(browser):
    pass
