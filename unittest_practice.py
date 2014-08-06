#!/usr/bin/env python  
#encoding: utf-8 

import unittest
import unittest_function

class mytest(unittest.TestCase):

	# Initialization
	def setUp(self):
		pass

	# Clear up
	def tearDown(self):
		pass

	# An instance for testing, the name should begin with 'test'
	def testsum(self):
		self.assertEqual(unittest_function.sum(1,2),2,'test sum fail')

	def testsub(self):
		self.assertEqual(unittest_function.sub(2,1),1,'test sub fail')



if __name__ == '__main__':
	unittest.main()