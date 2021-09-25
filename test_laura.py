import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from data_generator import *

main_page_link = 'https://laura-ashley.com.ua/'
login_page_link = 'https://laura-ashley.com.ua/Account/Login/'
registration_page_link = 'https://laura-ashley.com.ua/account/register'


def test_login_link_is_present(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason='Pop-up window for discounts until September 27')
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.gp_to_login_page()
    page.should_be_login_form()


@pytest.mark.positive
def test_guest_can_login(browser):
    mail = 'mail@mail.com'
    password = '1234'
    page = LoginPage(browser, login_page_link)
    page.open()
    page.fill_out_login_form(mail, password)
    page.should_be_logout_link()


wrong_login_data_list = generate_wrong_login_data()


@pytest.mark.negative
@pytest.mark.parametrize('wrong_data', wrong_login_data_list)
def test_login_error(browser, wrong_data):
    mail = wrong_data['mail']
    password = wrong_data['password']
    page = LoginPage(browser, login_page_link)
    page.open()
    page.fill_out_login_form(mail, password)
    page.should_be_warning_message()


@pytest.mark.positive
def test_guest_can_register(browser):
    registration_data = generate_right_registration_data()
    page = RegistrationPage(browser, registration_page_link)
    page.open()
    page.fill_out_registration_form(**registration_data)
    page.should_be_logout_link()


wrong_registration_data = generate_wrong_registration_data()


@pytest.mark.negative
@pytest.mark.parametrize('wrong_data', wrong_registration_data)
def test_guest_can_register(browser, wrong_data):
    page = RegistrationPage(browser, registration_page_link)
    page.open()
    page.fill_out_registration_form(**wrong_data)
    page.should_be_warning_message()