import allure

from page_objects.ProductCardPage import ProductCardPage


@allure.parent_suite("Проверка тестового магазина opencart")
@allure.suite("Тесты страницы карточки товара")
# @allure.sub_suite("Поиск элементов на странице карточки товара")
@allure.epic("Проверка магазина на opencart")
@allure.feature("Проверка карточки товара")
@allure.title("Поиск элементов на странице карточки товара")
@allure.description("""Тест проверяет наличие элементов на странице карточки товара""")
@allure.severity(allure.severity_level.NORMAL)
def tests_product_card_page(browser):
    product_card_page = ProductCardPage(browser).open()
    product_card_page.find_h1_product()
    product_card_page.find_button_add_to_cart()
    product_card_page.find_input_quantity()
    product_card_page.find_write_a_review()
    product_card_page.find_tab_description()
