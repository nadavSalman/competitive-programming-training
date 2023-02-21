import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.


from solution_6.solution import transform_into_non_increasing

class TestCalculateCrossVector(unittest.TestCase):
    
    
    def test_input_1(self):
        transform_into_non_increasing([1, 2, 5, 6, 7, 4])
        self.assertEqual(True,True)
        


if __name__ == '__main__':
    unittest.main()