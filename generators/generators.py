import os
import string

from dotenv import load_dotenv
from faker import Faker

load_dotenv()

MAIN_URL = 'https://b2c.passport.rt.ru'

valid_phone = os.getenv('phone')
valid_login = os.getenv('login')
valid_password = os.getenv('password')
valid_email = os.getenv('valid_email')
email_for_registration = os.getenv('email_for_registration')
valid_pass_reg = 'XqwZPIEA(4'

valid_ls = os.getenv('valid_ls')
fake_ls = os.getenv('fake_ls')

fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()

fake_en = Faker()
fake_password = fake_en.password()
fake_login = fake_en.user_name()
fake_email = fake_en.email()

fake_cn = Faker('zh_CN')


def generate_string_rus(n):
    chars_string = ''.join(fake_ru.words(nb=n))
    return chars_string


def generate_string_en(n):
    chars_string = ''.join(fake_en.words(nb=n))
    return chars_string


def english_chars():
    chars_string = ''.join(fake_en.words(nb=5))
    return chars_string


def russian_chars():
    chars_string = ''.join(fake_ru.words(nb=5))
    return chars_string


def chinese_chars():
    chars_string = ''.join(fake_cn.words(nb=5))
    return chars_string


def special_chars():
    return string.punctuation
