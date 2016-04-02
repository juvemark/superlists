# -*- coding: utf-8 -*-
from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
	@skip
	def test_connot_add_empty_list_items(self):
		# Edith visit main page and input a empty item

		# The main page refresh, and an error message shows

		# She input some words and submit again

		# She submit an empty item again

		# same error message shows

		# After input some words it works
		self.fail("write me!")
