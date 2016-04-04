# -*- coding: utf-8 -*-
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith visit main page and input a empty item
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		# The main page refresh, and an error message shows
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# She input some words and submit again
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# She submit an empty item again
		self.get_item_input_box().send_keys('\n')

		# same error message shows
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# After input some words it works
		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')
