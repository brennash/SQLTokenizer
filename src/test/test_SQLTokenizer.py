import re
import sys
import json
import logging
import unittest
import datetime
from SQLTokenizer import SQLTokenizer

class Test(unittest.TestCase):

	def test_initSetup_1(self):
		""" 
		Tests the test class itself to verify it is working. 
		Should all other tests fail, at least this test should pass.
		"""
		self.assertTrue(True)

	def test_initSetup_2(self):
		""" 
		Tests to see the class instantiates correctly.
		"""
		sqlTokenizer = SQLTokenizer()
		self.assertIsNotNone(sqlTokenizer)

def main():
    unittest.main()

if __name__ == '__main__':
    main()


