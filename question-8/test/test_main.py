import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.


from solution_8.solution import decode_atr

class TestQuestion8(unittest.TestCase):
    
    
    def test_one_middle_group(self):
        self.assertEqual(decode_atr('ab2[cd]e'),'abcdcde')

    def test_one_middle_group(self):
        self.assertEqual(decode_atr('ab2[cd]e'),'abcdcde')
    
    def test_one_middle_group(self):
        self.assertEqual(decode_atr('ab2[cd]e'),'abcdcde')


if __name__ == '__main__':
    unittest.main()