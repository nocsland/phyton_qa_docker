import allure

from page_objects.CatalogPage import CatalogPage


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты страницы каталога")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка каталога")
@allure.title("Поиск элементов на странице каталога")
@allure.description("""Тест проверяет наличие элементов на странице каталога""")
@allure.severity(allure.severity_level.NORMAL)
def tests_find_el_catalog(browser):
    catalog_page = CatalogPage(browser).open()
    catalog_page.find_top_menu()
    catalog_page.find_left_menu()
    catalog_page.find_link_product_compare()
    catalog_page.find_class_input_group()
    catalog_page.find_search_button()
