import unittest
from pyunitreport import HTMLTestRunner


import sys
import os
# sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)
# from solution import swap_by_prefix

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
from solution.solution import swap_by_prefix


class TestStringMethods(unittest.TestCase):

  def test_swap_with_prefix_within_both_strings_size(self):
    self.assertEqual(swap_by_prefix('aaabba','ababba',1,3), ('abaaabba','abba'))

  def test_swap_with_prefix_zero_to_s(self):
    self.assertEqual(swap_by_prefix('abababab','bbbbbbb',0,3),('bbbabababab','bbbb'))

  def test_swap_with_prefix_zero_to_t(self):
    self.assertEqual(swap_by_prefix('abababab','bbbbbbb',4,0),('abab','ababbbbbbbb'))

  def test_swap_s_with_t(self):
    self.assertEqual(swap_by_prefix('ababab','babababababababab',6,17),('babababababababab','ababab'))




'''
Tests report using : https://github.com/httprunner/PyUnitReport
'''
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='unit_tests_report'))  