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
		# 伊迪丝听说有一个很酷的在线待办事项应用， 她去看了这个应用的首页 
		self.browser.get('http://localhost:8090')

		# 她注意到网页的标题和头部都包括'TO-Do'
		assert 'To-Do' in browser.title

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