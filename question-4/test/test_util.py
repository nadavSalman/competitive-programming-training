import sys
import os
import unittest


#required for parent folder overview in order to get import parent subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_4.util import place_mine , map_status



class TestUtil(unittest.TestCase):

    def test_place_mine_map_middle(self):
        mine_map = "1110111"
        mine_map = place_mine(mine_map,3)
        #print('TestUtil / test_place_mine / mine_map -> ',mine_map)
        self.assertEqual(mine_map[3], "1")

    def test_place_mine_map_right(self):
        mine_map = "1110110"
        mine_map = place_mine(mine_map,mine_map.__len__() - 1)
        #print('TestUtil / test_place_mine / mine_map -> ',mine_map)
        self.assertEqual(mine_map[mine_map.__len__() - 1], "1")

    def test_place_mine_map_left(self):
        mine_map = "0110111"
        mine_map = place_mine(mine_map,0)
        #print('TestUtil / test_place_mine / mine_map -> ',mine_map)
        self.assertEqual(mine_map[0], "1")


    def test_map_status_clean_map(self):
        self.assertFalse(not map_status("0000000000"))


    def test_map_status_unclean_map(self):
        self.assertFalse(map_status("00010000100001100"))




if __name__ == '__main__':
    unittest.main()