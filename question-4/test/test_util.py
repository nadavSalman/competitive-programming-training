import sys
import os
import unittest


#required for parent folder overview in order to get import parent subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_4.solution import place_mine



class TestUtil(unittest.TestCase):



   
    def test_place_mine(self):
        mine_map = "1110111"
        mine_map = place_mine(mine_map,3)
        #print('TestUtil / test_place_mine / mine_map -> ',mine_map)
        self.assertEqual(mine_map[3], "1")





if __name__ == '__main__':
    unittest.main()