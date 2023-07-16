import time
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from data_generators.generators import MAIN_URL
from classes.locators import RegistrationLocators, AuthLocators


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = MAIN_URL
        self.driver.implicitly_wait(timeout)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def find_many_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def find_element_until_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator),
                                                      message=f'Element {locator} not clickable!')


class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.first_name = driver.find_element(*RegistrationLocators.FIRSTNAME_XPATH)
        self.last_name = driver.find_element(*RegistrationLocators.LASTNAME_XPATH)
        self.email = driver.find_element(*RegistrationLocators.ADDRESS_ID)
        self.password = driver.find_element(*RegistrationLocators.PASSWORD_ID)
        self.pass_conf = driver.find_element(*RegistrationLocators.PASSWORD_CONFIRM_XPATH)
        self.btn = driver.find_element(*RegistrationLocators.BUTTON_REGISTER_XPATH)

    def enter_firstname(self, value):
        self.first_name.send_keys(value)

    def enter_lastname(self, value):
        self.last_name.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        self.pass_conf.send_keys(value)

    def btn_click(self):
        self.btn.click()


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.USERNAME_ID)
        self.password = driver.find_element(*AuthLocators.PASSWORD_ID)
        self.btn = driver.find_element(*AuthLocators.LOGIN_ID)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_IN_XPATH)
        self.active_tab = driver.find_element(*AuthLocators.RT_TAB_CSS)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def btn_click_enter(self):
        self.btn.click()
        time.sleep(10)

    def enter_reg_page(self):
        self.reg_in.click()
        time.sleep(10)

    def active_tab(self):
        self.active_tab()
