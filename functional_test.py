# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# input http://localhost:8090 to access webpage
		self.browser.get('http://localhost:8090')

		# there is a 'TO-Do' in the title
		self.assertIn( 'To-Do', self.browser.title)
		head_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn( 'To-Do', head_text)

		# Application invide her to input an item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# Input "Buy peacock feather"
		inputbox.send_keys('Buy peacock feathers')

		# After Enter, page update
		# Form show "1. Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows =  table.find_element_by_tag_name('tr')
		self.assertTrue( any(row.text == '1: Buy peacock feathers' for row in rows))

		# Show another dialog and it is possible to input another item
		# She input "Use peacock feathers to make a fly"
		self.fail('Finish the test!')
		# Page update again, her list show two items

		# She saw a URL, and some explanation about this URL

		# She visit the URL and found the list still exists

		# End

if __name__=='__main__':
	unittest.main(warnings='ignore')