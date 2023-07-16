import pickle

import pytest

from generators.generators import (valid_phone,
                                        valid_login,
                                        valid_password,
                                        valid_ls,
                                        valid_email,
                                        valid_pass_reg,
                                        fake_email,
                                        fake_login,
                                        fake_phone,
                                        fake_ls,
                                        fake_password)
from classes.classes import AuthPage, AuthLocators

LINK_AFTER_AUTH = '/account_b2c/page'
ERROR_MESSAGE_INVALID_LOG_OR_PASS = 'Неверный логин или пароль'
ERROR_MESSAGES = [
    'Введите номер телефона',
    'Введите адрес, указанный при регистрации',
    'Введите логин, указанный при регистрации',
    'Введите номер вашего лицевого счета'
]


def test_auth_page_valid_email(browser):
    """Проверяем авторизацию пользователя по адресу почты и паролю"""
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass_reg)
    page.btn_click_enter()
    with open('auth_cookies.txt', 'wb') as cookies:
        pickle.dump(browser.get_cookies(), cookies)
    assert page.get_relative_link() == LINK_AFTER_AUTH


@pytest.mark.parametrize('data_types', [valid_phone, valid_login],
                         ids=['valid phone', 'valid login'])
def test_auth_page_valid_data_types(browser, data_types):
    """Проверяем авторизацию пользователя по номеру телефона, логину и паролю."""
    page = AuthPage(browser)
    page.enter_username(data_types)
    page.enter_password(valid_password)
    page.btn_click_enter()
    assert page.get_relative_link() == LINK_AFTER_AUTH


@pytest.mark.parametrize('data_types', [valid_phone,
                                        valid_email,
                                        valid_login,
                                        valid_ls],
                         ids=['phone',
                              'email',
                              'login',
                              'ls'])
def test_active_tabs_switch(browser, data_types):
    """Проверяем автоматическое переключение таблиц выбора способа авторизации(тел/почта/логин/лицевой счет)"""
    page = AuthPage(browser)
    page.enter_username(data_types)
    page.enter_password(valid_password)
    if data_types == valid_phone:
        assert browser.find_element(*AuthLocators.RT_TAB_CSS).text == 'Телефон'
    elif data_types == valid_email:
        assert browser.find_element(*AuthLocators.RT_TAB_CSS).text == 'Почта'
    elif data_types == valid_login:
        assert browser.find_element(*AuthLocators.RT_TAB_CSS).text == 'Логин'
    else:
        assert browser.find_element(*AuthLocators.RT_TAB_CSS).text == 'Лицевой счет'


def test_auth_page_invalid_email(browser):
    """Проверяем авторизацию пользователя с некорректным адресом почты"""
    page = AuthPage(browser)
    page.enter_username(fake_email)
    page.enter_password(valid_pass_reg)
    page.btn_click_enter()
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.FORM_ERROR_MESSAGE_XPATH)
    assert error_mess.text == ERROR_MESSAGE_INVALID_LOG_OR_PASS


@pytest.mark.parametrize('data_types', [fake_phone, fake_login, fake_ls],
                         ids=['fake phone', 'fake login', 'fake service account'])
def test_auth_page_invalid_phone_login_account(browser, data_types):
    """Проверям авторизацию пользователя с некорректными данными номера телефона, логина и пароля"""
    page = AuthPage(browser)
    page.enter_username(data_types)
    page.enter_password(valid_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.FORM_ERROR_MESSAGE_XPATH)
    assert error_mess.text == ERROR_MESSAGE_INVALID_LOG_OR_PASS


def test_auth_page_empty_entry_field(browser):
    """Проверяем авторизацию пользователя с пустой строкой и корректным паролем"""
    page = AuthPage(browser)
    page.enter_username('')
    page.enter_password(valid_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.FORM_ERROR_MESSAGE_XPATH)
    assert error_mess.text in ERROR_MESSAGES


@pytest.mark.parametrize('username', [valid_phone, valid_email, valid_login],
                         ids=['valid phone', 'valid login', 'valid email'])
def test_auth_page_invalid_password(browser, username):
    """Проверяем авторизацию пользователя с некорректным паролем"""
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(fake_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.FORM_ERROR_MESSAGE_XPATH)
    assert error_mess.text == 'Неверный логин или пароль'


def test_auth_page_invalid_format_phone(browser):
    """Проверяем авторизацию пользователя  с некорректным номером телефона"""
    page = AuthPage(browser)
    page.enter_username(fake_phone[:-2])
    page.enter_password(valid_password)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.FORM_ERROR_MESSAGE_XPATH)
    assert error_mess.text == 'Неверный формат телефона'
