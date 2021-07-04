from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    path = '/index.php?route=product/product&path=57&product_id=49'

    def find_h1_product(self):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(.,"Tweet")]')))
        self.browser.find_element_by_xpath('//h1[contains(.,"Samsung Galaxy Tab 10.1")]')
        self.logger.info("element was found")
        return self

    def find_button_add_to_cart(self):
        self.browser.find_element_by_xpath('//*[@id="button-cart"]')
        self.logger.info("element was found")
        return self

    def find_input_quantity(self):
        self.browser.find_element_by_id('input-quantity')
        self.logger.info("element was found")
        return self

    def find_write_a_review(self):
        self.browser.find_element_by_link_text('Write a review')
        self.logger.info("element was found")
        return self

    def find_tab_description(self):
        self.browser.find_element_by_id('tab-description')
        self.logger.info("element was found")
        return self
