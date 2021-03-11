import unittest
from pyunitreport import HTMLTestRunner

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_4.util import manual_activation


class TestManualActivation(unittest.TestCase):
  def test_left_activation(self):
    mine_test = ['1','1','0']
    manual_activation(mine_test,0)
    self.assertEqual(mine_test,['0','0','0'])



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='unit_tests_report'))