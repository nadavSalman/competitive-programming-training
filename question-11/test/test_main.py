import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_10.solution import BinaryExecuter

class TestQuestion10(unittest.TestCase):
    def setUp(self):
        self.binary_executer = BinaryExecuter([])
    
    
    def test_best_case(self):
        self.binary_executer.set_array([0,0,0,0,0,0,0,0])
        self.assertEqual(self.binary_executer.binary_array_partition(),[0, len(self.binary_executer.get_array())-1])


    
    def test_avarage_case_a(self):
        self.binary_executer.set_array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        self.assertEqual(self.binary_executer.binary_array_partition(),[2, 7])


if __name__ == '__main__':
    unittest.main()         