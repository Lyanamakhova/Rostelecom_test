# Запуск тестов python -m pytest -v --driver Chrome --driver-path D:\Test\chromedriver-win64\chromedriver.exe tests\test_registration_page.py
import pytest
from pages.registration_page import RegistrationPage
from pages.locators import AuthLocators
from settings import *


def test_page_left_registration(selenium):
    """Проверка, что левая часть формы «Регистрация» содержит логотип и продуктовый слоган кабинета."""
    try:
        page_reg = RegistrationPage(selenium)
        assert page_reg.page_left_registration.text != ''
    except AssertionError:
        print('Элемент отсутствует в левой части формы')


def test_elements_of_registr(selenium):
    """Проверка, что блок регистрации содержит основные элементы:
    поля ввода: Имя, Фамилия, Регион, email, Пароль, Подтверждение пароля; кнопка "Продолжить"."""
    try:
        page_reg = RegistrationPage(selenium)
        card_of_reg = [page_reg.first_name, page_reg.last_name, page_reg.address_registration,
                       page_reg.email_registration, page_reg.passw_registration,
                       page_reg.passw_registration_confirm, page_reg.registration_btn]
        for i in range(len(card_of_reg)):
            assert page_reg.first_name in card_of_reg
            assert page_reg.last_name in card_of_reg
            assert page_reg.email_registration in card_of_reg
            assert page_reg.address_registration in card_of_reg
            assert page_reg.passw_registration in card_of_reg
            assert page_reg.passw_registration_confirm in card_of_reg
            assert page_reg.registration_btn in card_of_reg
    except AssertionError:
        print('Элемент отсутствует в форме «Регистрация»')


def test_names_elements_of_registr(selenium):
    """TC-13 Названия элементов блока регистрации формы «Регистрация» соответствуют Требованию."""
    try:
        page_reg = RegistrationPage(selenium)
        assert 'Имя' in page_reg.card_of_registration.text
        assert 'Фамилия' in page_reg.card_of_registration.text
        assert 'Регион' in page_reg.card_of_registration.text
        assert 'E-mail или мобильный телефон' in page_reg.card_of_registration.text
        assert 'Пароль' in page_reg.card_of_registration.text
        assert 'Подтверждение пароля' in page_reg.card_of_registration.text
        assert 'Продолжить' in page_reg.card_of_registration.text
    except AssertionError:
        print('Название элемента в форме «Регистрация» не соответствует Требованию')


def test_registr_by_valid_data(selenium):
    """TC-14 Регистрация пользователя с валидными данными"""
    page_reg = RegistrationPage(selenium)
    page_reg.first_name.send_keys(Settings.f_name)
    page_reg.first_name.clear()
    page_reg.last_name.send_keys(Settings.l_name)
    page_reg.last_name.clear()
    page_reg.email_registration.send_keys(Settings.valid_email_for_reg)
    page_reg.email_registration.clear()
    page_reg.passw_registration.send_keys(Settings.valid_password)
    page_reg.passw_registration.clear()
    page_reg.passw_registration_confirm.send_keys(Settings.valid_password)
    page_reg.passw_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert page_reg.find_other_element(*AuthLocators.email_confirm).text == 'Подтверждение email'



def test_registr_by_invalid_data(selenium):
    """Регистрация пользователя по email, который уже был использован ранее для регистрации"""
    page_reg = RegistrationPage(selenium)
    page_reg.first_name.send_keys(Settings.f_name)
    page_reg.first_name.clear()
    page_reg.last_name.send_keys(Settings.l_name)
    page_reg.last_name.clear()
    page_reg.email_registration.send_keys(Settings.valid_email)
    page_reg.email_registration.clear()
    page_reg.passw_registration.send_keys(Settings.valid_password)
    page_reg.passw_registration.clear()
    page_reg.passw_registration_confirm.send_keys(Settings.valid_password)
    page_reg.passw_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert "Учётная запись уже существует" in page_reg.find_other_element(*AuthLocators.error_account_exists).text


@pytest.mark.parametrize("valid_first_name",
                         [
                             (Settings.russian_generate_string) * 2
                             , (Settings.russian_generate_string) * 3
                             , (Settings.russian_generate_string) * 15
                             , (Settings.russian_generate_string) * 29
                             , (Settings.russian_generate_string) * 30
                         ],
                         ids=
                         [
                             'russ_symbols=2', 'russ_symbols=3', 'russ_symbols=15',
                             'russ_symbols=29', 'russ_symbols=30'
                         ])
def test_first_name_by_valid_data(selenium, valid_first_name):
    """ Проверка поля ввода "Имя" формы «Регистрация» валидными данными:
    буквы кириллицы в количестве = 2 ; 3 ; 15 ; 29 ; 30 ."""
    page_reg = RegistrationPage(selenium)
    page_reg.first_name.send_keys(valid_first_name)
    page_reg.first_name.clear()
    page_reg.registration_btn.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in page_reg.container_f_name.text


@pytest.mark.parametrize("invalid_first_name",
                         [
                             (Settings.russian_generate_string) * 1
                             , (Settings.russian_generate_string) * 31
                             , (Settings.russian_generate_string) * 260
                             , (Settings.empty), (Settings.numbers)
                             , (Settings.latin_generate_string)
                             , (Settings.chinese_chars), (Settings.special_chars)
                         ],
                         ids=
                         [
                             'russ_symbols=1', 'russ_symbols=31', 'russ_symbols=260',
                             'empty', 'numbers', 'latin_symbols', 'chinese_symbols', 'special_symbols'
                         ])
def test_first_name_by_invalid_data(selenium, invalid_first_name):
    """ Проверка поля ввода "Имя" формы «Регистрация» невалидными данными:
    пустое значение;
    буквы кириллицы в количестве = 1 ; 31 ; 500 ;
    буквы латиницы; иероглифы; спецсимволы; числа."""
    page_reg = RegistrationPage(selenium)
    page_reg.first_name.send_keys(invalid_first_name)
    page_reg.first_name.clear()
    page_reg.registration_btn.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in \
           page_reg.find_other_element(*AuthLocators.error_first_name).text


@pytest.mark.parametrize("valid_password",
                         [(Settings.passw1), (Settings.passw2), (Settings.passw3)],
                         ids=['valid_symbols=8', 'valid_symbols=15', 'valid_symbols=20'])
def test_last_name_by_valid_data(selenium, valid_password):
    """ Проверка поля ввода "Пароль" формы «Регистрация» валидными данными:
    символы из букв латиницы прописью и строчные+числа в количестве = 8 ; 15 ; 20 ."""
    page_reg = RegistrationPage(selenium)
    page_reg.passw_registration.send_keys(valid_password)
    page_reg.passw_registration.clear()
    page_reg.registration_btn.click()

    assert 'Длина пароля должна быть не менее 8 символов' and \
           'Длина пароля должна быть не более 20 символов' and \
           'Пароль должен содержать хотя бы одну заглавную букву' and \
           'Пароль должен содержать хотя бы одну прописную букву' and \
           'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' not in \
           page_reg.passw_registration.text


def test_passw_registration_confirm_valid_data(selenium):
    """ Проверка поля ввода "Пароль" и "Подтвердить пароль" формы «Регистрация» валидными данными
    (пароли совпадают)."""
    page_reg = RegistrationPage(selenium)
    page_reg.passw_registration.send_keys(Settings.passw1)
    page_reg.passw_registration.clear()
    page_reg.passw_registration_confirm.send_keys(Settings.passw1)
    page_reg.passw_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert 'Пароли не совпадают' not in page_reg.container_passw_confirm.text


def test_passw_registration_confirm_invalid_data(selenium):
    """ Проверка поля ввода "Пароль" и "Подтвердить пароль" формы «Регистрация» невалидными данными
    (пароли не совпадают)."""
    page_reg = RegistrationPage(selenium)
    page_reg.passw_registration.send_keys(Settings.passw1)
    page_reg.passw_registration.clear()
    page_reg.passw_registration_confirm.send_keys(Settings.passw2)
    page_reg.passw_registration_confirm.clear()
    page_reg.registration_btn.click()

    assert 'Пароли не совпадают' in page_reg.find_other_element(*AuthLocators.error_passw_confirm).text