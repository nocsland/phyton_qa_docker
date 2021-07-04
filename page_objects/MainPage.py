from page_objects.BasePage import BasePage


class MainPage(BasePage):
    path = '/'

    def find_h1_your_store(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_xpath('//*[@id="logo"]/h1/a')

    def find_name_search(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_name('search')

    def find_id_cart(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_id('cart')

    def find_link_iphone(self):
        self.logger.info('element was found')
        return self.browser.find_element_by_link_text('iPhone')

    def find_part_link_terms(self):
        self.logger.info('element was found')
        return self.browser.find_elements_by_partial_link_text('Terms & Cond')

    def click_add_user(self):
        self.browser.find_element_by_css_selector('.fa-user').click()
        self.logger.info('dropdown menu was clicked')
        self.browser.find_element_by_link_text('Register').click()
        self.logger.info('Register was clicked')
        return self

    def fill_register_form(self, f_name, l_name, email, phone, password):
        self.browser.find_element_by_id('input-firstname').clear()
        self.browser.find_element_by_id('input-firstname').send_keys(f_name)
        self.browser.find_element_by_id('input-lastname').clear()
        self.browser.find_element_by_id('input-lastname').send_keys(l_name)
        self.browser.find_element_by_id('input-email').clear()
        self.browser.find_element_by_id('input-email').send_keys(email)
        self.browser.find_element_by_id('input-telephone').clear()
        self.browser.find_element_by_id('input-telephone').send_keys(phone)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_id('input-confirm').clear()
        self.browser.find_element_by_id('input-confirm').send_keys(password)
        self.logger.info('all fields register form was filled')
        return self

    def click_agree_and_continue(self):
        self.browser.find_element_by_name('agree').click()
        self.browser.find_element_by_css_selector('.btn-primary').click()
        self.browser.find_element_by_link_text('Continue').click()
        self.logger.info('agree and continue was clicked')
        return self
