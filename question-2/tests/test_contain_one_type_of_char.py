import unittest
from pyunitreport import HTMLTestRunner




import sys
import os

#sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
from solution.solution import contain_one_type_of_char


#from solution import contain_one_type_of_char


class TestStringMethods(unittest.TestCase):

  def test_one_char_multiple_times(self):
    self.assertEqual(contain_one_type_of_char('aaaaaa'),True)
  
  def test_empty_str(self):
    self.assertEqual(contain_one_type_of_char(''),True)
    
  def test_one_char(self):
    self.assertEqual(contain_one_type_of_char('a'),True)

  def test_two_cainds_of_chars_in_length_two(self):
    self.assertEqual(contain_one_type_of_char('ab'),False)

  def test_two_cainds_of_chars_in_length_greater_then_two(self):
    self.assertEqual(contain_one_type_of_char('aaababbbaaa'),False)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='unit_tests_report'))