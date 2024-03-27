import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.



class TestQuestion8(unittest.TestCase):
    
    
    def test_test(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()