#!/usr/bin/env python  
#encoding: utf-8 

import unittest
import unittest_function

# class mytest(unittest.TestCase):
# '''
# First try: unittest on a function
# '''
# 	# Initialization
# 	def setUp(self):
# 		pass

# 	# Clear up
# 	def tearDown(self):
# 		pass

# 	# An instance for testing, the name should begin with 'test'
# 	def testsum(self):
# 		self.assertEqual(unittest_function.sum(1,2),2,'test sum fail')

# 	def testsub(self):
# 		self.assertEqual(unittest_function.sub(2,1),1,'test sub fail')
class mytest(unittest.TestCase):
	# Initialization
	# 实例化模块中的类
	def setUp(self):
		self.tclass = unittest_function.myclass()

	# Clear up
	def tearDown(self):
		pass

	def testSum(self):
		self.assertEqual(self.tclass.Sum(1,2),3)
		
if __name__ == '__main__':
	unittest.main()