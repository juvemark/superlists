# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# input http://localhost:8090 to access webpage
		self.browser.get(self.live_server_url)
		#time.sleep(10)

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
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# Show another dialog and it is possible to input another item
		# She input "Use peacock feathers to make a fly"

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# Page update again, her list show two items
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Now a new user Francsis visit the user
		self.browser.close()
		self.browser=webdriver.Firefox()
		# He visis the front page
		# Cannot see the list of her
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		#He input a new item and create a list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# He get his onw URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# Still no Edith list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		# She saw a URL, and some explanation about this URL

		# She visit the URL and found the list still exists

		# End
	def test_layout_and_styling(self):
		#Edith visit the main page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)

		#She finds input box show in the middle perfectly
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)

		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)
