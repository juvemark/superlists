from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait
TEST_EMAIL = 'edith@mockmyid.com'

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        # Edith visit this super good website
        # There is a sign in link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # Persona dialog shows
        self.switch_to_new_window('Mozilla Persona')

        #Edith use her email to log in
        self.browser.find_element_by_id('authentication_email').send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        #Persona dialog close
        self.switch_to_new_window('To-Do')

        #She found she has already log in
        self.wait_to_be_logged_in(email='edith@mockmyid.com')

        #refresh and she dfind it is real
        self.browser.refresh()
        self.wait_to_be_logged_in(email='edith@mockmyid.com')

        #She click log out
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email='edith@mockmyid.com')

        # refresh still log out
        self.browser.refresh()
        self.wait_to_be_logged_out(email='edith@mockmyid.com')

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries>0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

