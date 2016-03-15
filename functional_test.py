# -*- coding: utf-8 -*-
from selenium import webdriver
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
		assert 'To-Do' in self.browser.title

		# Application invide her to input an item

		# Input "Buy peacock feather"

		# After Enter, page update
		# Form show "1. Buy peacock feathers"

		# Show another dialog and it is possible to input another item
		# She input "Use peacock feathers to make a fly"

		# Page update again, her list show two items

		# She saw a URL, and some explanation about this URL

		# She visit the URL and found the list still exists

		# End

if __name__=='__main__':
	unittest.main(warnings='ignore')