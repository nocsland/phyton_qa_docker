from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    path = '/admin/'

    def find_logo_open_cart(self):
        self.browser.find_element_by_xpath("//img[@alt='OpenCart']")
        self.logger.info("element was found")
        return self

    def find_input_username(self):
        self.browser.find_element_by_name('username')
        self.logger.info("element was found")
        return self

    def find_h1_in_form(self):
        self.browser.find_element_by_xpath('//h1[contains(.," Please enter your login details.")]')
        self.logger.info("element was found")
        return self

    def find_input_password(self):
        self.browser.find_element_by_id('input-password')
        self.logger.info("element was found")
        return self

    def find_login_button(self):
        self.browser.find_element_by_xpath('//button[contains(.," Login")]')
        self.logger.info("element was found")
        return self

    def login(self, login, password):
        self.browser.find_element_by_name('username').clear()
        self.browser.find_element_by_name('username').send_keys(login)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_xpath('//button[contains(.," Login")]').click()
        self.logger.info("login completed")
        return self

    def goto_all_product(self):
        self.browser.find_element_by_id('menu-catalog').click()
        self.browser.find_element_by_xpath('//a[contains(text(),"Products")]').click()
        self.logger.info('navigated to the product page')
        return self

    def click_add_product(self):
        self.browser.find_element_by_css_selector('.fa-plus').click()
        self.logger.info('clicked add')
        return self

    def fill_general_form_product(self, name, title):
        self.browser.find_element_by_id('input-name1').send_keys(name)
        self.browser.find_element_by_id('input-meta-title1').send_keys(title)
        self.logger.info('the name and title fields are filled')
        return self

    def goto_data_tab(self):
        self.browser.find_element_by_link_text('Data').click()
        self.logger.info('navigated to the data tab')
        return self

    def fill_data_tab_product(self, model):
        self.browser.find_element_by_id('input-model').send_keys(model)
        self.logger.info('the model field is filled')
        return self

    def click_save_product(self):
        self.browser.find_element_by_css_selector('.fa-save').click()
        self.logger.info('product was saved')
        return self

    def find_and_delete_product(self):
        self.browser.find_element_by_xpath('//tr[20]/td/input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
        self.logger.info('product was deleted')
        return self
