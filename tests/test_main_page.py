import allure

from page_objects.MainPage import MainPage


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты главной страницы")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка title")
@allure.title("Проверка title главной страницы")
@allure.description("""Тест проверяет title главной страницы""")
@allure.severity(allure.severity_level.CRITICAL)
def test_is_title(browser):
    main_page = MainPage(browser).open()
    main_page.verify_title('Your Store')


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты главной страницы")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка главной страницы")
@allure.title("Поиск элементов на главной странице")
@allure.description("""Тест проверяет наличие элементов на главной странице""")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_el_main(browser):
    main_page = MainPage(browser).open()
    main_page.find_h1_your_store()
    main_page.find_name_search()
    main_page.find_id_cart()
    main_page.find_link_iphone()
    main_page.find_part_link_terms()


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты главной страницы")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка главной страницы")
@allure.title("Добавление нового пользователя")
@allure.description("""Тест проверяет возможность добавить нового пользователя""")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_user(browser):
    main_page = MainPage(browser).open()
    allure.attach.file(source='tests/attachments/add_user.png', attachment_type=allure.attachment_type.PNG)
    main_page.click_add_user()
    main_page.fill_register_form('Ivan15', 'Ivanov15', 'test15@ya.ru', '+79000551135', 'test')
    main_page.click_agree_and_continue()
    main_page.verify_title('My Account')


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты главной страницы")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка главной страницы")
@allure.title("Переключение валюты")
@allure.description("""Тест проверяет возможность переключить валюту цен и расчетов""")
@allure.severity(allure.severity_level.NORMAL)
def test_switch_currency(browser):
    main_page = MainPage(browser).open()
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="EUR"]')
    main_page.click_to_currency('EUR')
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="GBP"]')
    main_page.click_to_currency('GBP')
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="USD"]')
    main_page.click_to_currency('USD')
