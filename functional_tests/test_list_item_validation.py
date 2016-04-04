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
		error = self.get_error_element()
		self.assertEqual(error.text, "You can't have an empty list item")

		# She input some words and submit again
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# She submit an empty item again
		self.get_item_input_box().send_keys('\n')

		# same error message shows
		error = self.get_error_element()
		self.assertEqual(error.text, "You can't have an empty list item")

		# After input some words it works
		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

	def test_cannot_add_duplicate_items(self):
		# Edith visit main page and new a list
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Buy wellies\n')
		self.check_for_row_in_list_table('1: Buy wellies')

		# She input a duplicate item uncarefully
		self.get_item_input_box().send_keys('Buy wellies\n')

		# She saw an error message
		self.check_for_row_in_list_table('1: Buy wellies')
		error = self.get_error_element()
		self.assertEqual(error.text, "You've already got this in your list")

	def test_error_messages_are_cleared_on_input(self):
		# Edith new a list, but wrong way, so there is an error message
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')
		error = self.get_error_element()
		self.assertTrue(error.is_displayed())

		#In order to make it correct, she starts to input content
		self.get_item_input_box().send_keys('a')

		# The error message disappear
		error = self.get_error_element()
		self.assertFalse(error.is_displayed())

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')