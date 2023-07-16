from selenium.webdriver.common.by import By


class AuthLocators:
    """Перечень локаторов для раздела авторизации"""
    USERNAME_ID = (By.ID, 'username')
    PASSWORD_ID = (By.ID, 'password')
    LOGIN_ID = (By.ID, 'kc-login')
    FORM_ERROR_MESSAGE_XPATH = (By.XPATH, "//span[@id='form-error-message']")
    MESSAGE_ERROR_CSS = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    AUTH_IN_XPATH = (By.XPATH, "//a[@id='kc-register']")
    AUTH_IN_CODE_ID = (By.ID, 'back_to_otp_btn')
    RT_TAB_CSS = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    FORGOT_PASSWORD_ID = (By.ID, 'forgot_password')


class RegistrationLocators:
    """Перечень локаторов для раздела регистрации"""
    FIRSTNAME_XPATH = (By.XPATH, "//input[@name='firstName']")
    LASTNAME_XPATH = (By.XPATH, "//input[@name='lastName']")
    CITY_XPATH = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    ADDRESS_ID = (By.ID, 'address')
    PASSWORD_ID = (By.ID, 'password')
    PASSWORD_CONFIRM_XPATH = (By.XPATH, "//input[@id='password-confirm']")
    BUTTON_REGISTER_XPATH = (By.XPATH, "//button[@name='register']")
    CARD_XPATH = (By.XPATH, "//h2[@class='card-modal__title']")
