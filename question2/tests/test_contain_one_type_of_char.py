import unittest
from pyunitreport import HTMLTestRunner


import sys
import os
sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)
from solution import contain_one_type_of_char
class TestStringMethods(unittest.TestCase):

  def test_ss(self):
    self.assertEqual(1,1)



'''
Tests report using : https://github.com/httprunner/PyUnitReport
'''
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='unit_tests_report'))