import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from classes.classes import AuthPage


@pytest.fixture(autouse=True)
def browser():
    s = Service(executable_path='/tests_rostelecom/chromedriver')
    driver = webdriver.Chrome(service=s)

    yield driver
    driver.quit()


@pytest.fixture()
def get_code_from_email():
    pass


@pytest.fixture()
def get_registration_page(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
