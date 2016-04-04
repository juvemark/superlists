# -*- coding: utf-8 -*-
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
	def test_layout_and_styling(self):
		#Edith visit the main page
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,768)

		#She finds input box show in the middle perfectly
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)

		inputbox.send_keys('testing\n')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)