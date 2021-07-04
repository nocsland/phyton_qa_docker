import allure

from page_objects.LoginPage import LoginPage


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты страницы авторизации")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка наличия элементов на странице логина")
@allure.title("Поиск элементов на странице логина")
@allure.description("""Тест проверяет наличие элементов на странице логина""")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_page(browser, pytestconfig):
    login_page = LoginPage(browser).open()
    login_page.find_input_email()
    login_page.find_continue_button()
    login_page.find_input_password()
    login_page.find_forgotten_password()
    login_page.find_login_button()
