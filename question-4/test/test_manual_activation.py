import unittest
from pyunitreport import HTMLTestRunner

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_4.util import manual_activation


class TestManualActivationGroupedMines(unittest.TestCase):
  
  def test_left_activation(self):
    mine_test = ['1','1','0']
    manual_activation(mine_test,0)
    self.assertEqual(mine_test,['0','0','0'])

  def test_middle_activation(self):
    mine_test = ['0','1','1','1','0']
    manual_activation(mine_test,3)
    self.assertEqual(mine_test,['0','0','0','0','0'])

  def test_right_activation(self):
    mine_test = ['0','1','1']
    manual_activation(mine_test,2)
    self.assertEqual(mine_test,['0','0','0'])

class TestManualActivationSeparatedMines(unittest.TestCase):

  def test_separated_mines_one_activation(self):
    mine_test = ['1','0','1','0','1']
    manual_activation(mine_test,0)
    self.assertEqual(mine_test,['0','0','1','0','1'])

  def test_separated_mines_multiple_activation(self):
      mine_test = ['1','0','1','0','1']
      manual_activation(mine_test,0)
      manual_activation(mine_test,len(mine_test) - 1)
      self.assertEqual(mine_test,['0','0','1','0','0'])


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='unit_tests_report'))