import pytest
from selenium.webdriver.common.by import By

from generators import generators
from classes.classes import AuthPage, RegPage, AuthLocators


def test_open_registration_page(browser):
    """Открываем страницу регистрации"""
    page = AuthPage(browser)
    page.enter_reg_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_new_user_registration(browser, get_code_from_email, get_registration_page):
    """Регистрируем нового пользователя"""
    page = RegPage(browser)
    page.enter_firstname(generators.fake_firstname)
    page.enter_lastname(generators.fake_lastname)
    page.enter_email(generators.email_for_registration)
    page.enter_password(generators.fake_password)
    page.enter_pass_conf(generators.fake_password)
    page.btn_click()
    code = get_code_from_email
    browser.implicitly_wait(10)
    for i in range(0, 6):
        browser.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(code[i])
        browser.implicitly_wait(5)
    assert page.get_relative_link() == '/account_b2c/page'


def test_get_registration_diff_pass_and_pass_conf(browser, get_registration_page):
    """Проверяем ответ системы на несовпадение пароля и его подтверждения"""
    page = RegPage(browser)
    page.enter_firstname(generators.fake_firstname)
    page.enter_lastname(generators.fake_lastname)
    page.enter_email(generators.fake_email)
    page.enter_password(generators.fake_password)
    page.enter_pass_conf(generators.valid_pass_reg)
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.MESSAGE_ERROR_CSS)
    assert error_mess.text == 'Пароли не совпадают'


@pytest.mark.parametrize('phone', ['', 1, 7111111111,
                                   generators.generate_string_rus(11),
                                   generators.special_chars()],
                         ids=['empty', 'one digit', 'no 1 digit', 'string', 'specials'])
def test_get_registration_invalid_format_phone(browser, phone, get_registration_page):
    """Регистрируем пользователя с некорректным(несуществующим) адресом почты"""
    page = RegPage(browser)
    page.enter_firstname(generators.fake_firstname)
    page.enter_lastname(generators.fake_lastname)
    page.enter_email(phone)
    page.enter_password(generators.fake_password)
    page.enter_pass_conf(generators.fake_password)
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.MESSAGE_ERROR_CSS)
    assert error_mess.text == ('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, '
                               'или email в формате example@email.ru')


@pytest.mark.parametrize('firstname, lastname', [
    ('', ''),
    (generators.generate_string_rus(1), generators.generate_string_rus(1)),
    (generators.generate_string_rus(31), generators.generate_string_rus(31)),
    (generators.generate_string_rus(256), generators.generate_string_rus(256)),
    (generators.english_chars(), generators.english_chars()),
    (generators.chinese_chars(), generators.chinese_chars()),
    (generators.special_chars(), generators.special_chars()),
    (11111, 11111)
],
                         ids=['empty', 'one char', '31 chars', '256 chars', 'english', 'chinese',
                              'special', 'number'])
def test_registration_with_invalid_format_firstname(browser, firstname, lastname, get_registration_page):
    """Регистрируем пользователя с некорректными данными"""
    page = RegPage(browser)
    page.enter_firstname(firstname)
    page.enter_lastname(lastname)
    page.enter_email(generators.fake_email)
    page.enter_password(generators.fake_password)
    page.enter_pass_conf(generators.fake_password)
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.MESSAGE_ERROR_CSS)
    assert error_mess.text == 'Необходимо заполнить поле кириллицей, от 2 до 30 символов.'






