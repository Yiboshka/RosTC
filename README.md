### Дипломный проект разделам авторизации и регистрации сайта"Ростелеком."

#### Чтобы запустить тесты, необходимо:
1. Клонировать репозиторий `git clone <ssh>`
2. Развернуть виртуальное окружение `python -m venv venv`
3. Установить зависимости из файла requirements.txt `pip install requirements.txt`
4. Создать файл **.env** с переменными окружения: phone, login, password, valid_email, valid_ls, fake_ls и email_for_registration 
5. Проверить совместимость драйвера для запуска
#### Инструменты, которые использовались при создании автотестов:
1. Pytest для написания автоматических тестов
2. Selenium для автоматизации действий браузера при тестировании. 
3. Faker для генерации тестовых данных.
