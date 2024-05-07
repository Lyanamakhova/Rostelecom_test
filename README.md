Проект:  Тестирование Личного кабинета Ростелеком
Объект тестирования: https://b2c.passport.rt.ru
В рамках данного проекта был протестирован интерфейс авторизации и регистрации в личном кабинете от заказчика Ростелеком Информационные Технологии по предоставленным требованиям к сайту.
Разработаны тест-кейсы (более 15) , оформлено описание обнаруженных дефектов с использованием шаблона.
При тестировании использовались следующие инструменты: PageObject, Selenium и PyTest.

В корневой папке находятся файлы settings.py с тестовыми данными, requirements.txt для установки необходимых для тестирования библиотек.

Папка tests содержит файлы для запуска автотестов: test_auth_page.py - тесты для страницы авторизация, test_registration_page.py - тесты для страницы регистрация.

Папка pages содержит следующие файлы: locators.py - список локаторов на веб страницах, base_page.py - базовая страница, от которой унаследованы все остальные классы, auth_page.py - содержит класс для страницы авторизация, registr_page.py - содержит класс для страницы регистрация.

Перед запуском тестов требуется установить необходимые библиотеки командой:

pip install -r requirements.txt Запуск тестов при помощи команд в консоли:

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py 
python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_registr_page.py

Тесты внутри проекта содержат описание своего назначения.

Тестовые сценарии страницы авторизация (test_auth_page.py):

Проверка различных элементов страницы на их наличие и название согласно требованию. Проверка табов меню авторизация. При переходе по ссылкам "Забыл пароль" и "Зарегистрироваться" открываются соответствующие страницы. Проверка аутентификации пользователя с валидными и невалидными данными. 

Тестовые сценарии страницы регистрация (test_registr_page.py):

Проверка различных элементов страницы на их наличие и название согласно требованию. Сценарии регистрации пользователя с валидными данными ("Имя" и "Фамилия" - буквы кириллицы либо тире). Сценарии регистрации пользователя с данными, которы были использованы ранее. Проверки полей ввода валидными и невалидными данными.
