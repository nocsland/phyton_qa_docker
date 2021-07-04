from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    path = '/index.php?route=account/login'

    def find_input_email(self):
        self.browser.find_element_by_id('input-email')
        self.logger.info('input_email was found')
        return self

    def find_continue_button(self):
        self.browser.find_element_by_link_text('Continue')
        self.logger.info('continue button was found')
        return self

    def find_input_password(self):
        self.browser.find_element_by_xpath('//*[@id="input-password"]')
        self.logger.info('input-password was found')
        return self

    def find_forgotten_password(self):
        self.browser.find_element_by_link_text('Forgotten Password')
        self.logger.info('Forgotten Password was found')
        return self

    def find_login_button(self):
        self.browser.find_element_by_xpath('//*[@id="content"]//form/input')
        self.logger.info('login button was found')
        return self
