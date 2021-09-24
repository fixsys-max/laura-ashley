import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

main_page_link = 'https://laura-ashley.com.ua/'
login_page_link = 'https://laura-ashley.com.ua/Account/Login/'


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


def test_guest_can_login(browser):
    mail = 'mail@mail.com'
    password = '1234'
    page = LoginPage(browser, login_page_link)
    page.open()
    page.fill_out_login_form(mail, password)
    page.should_be_logout_link()


wrong_login_data_list = [{"mail": '', 'password': ''},
                         {'mail': 'mail@mail.com', 'password': ''},
                         {'mail': '12345@mail.com', 'password': 'Qwerty1@'}]


@pytest.mark.negative
@pytest.mark.parametrize('wrong_data', wrong_login_data_list)
def test_login_error(browser, wrong_data):
    mail = wrong_data['mail']
    password = wrong_data['password']
    page = LoginPage(browser, login_page_link)
    page.open()
    page.fill_out_login_form(mail, password)
    page.should_be_warning_message()
