import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution import PuzzleSolution

class TestCheckBlock(unittest.TestCase):

    '''
    Declare global variables
    '''


    def __init__(self):
        self.game_board = PuzzleSolution(9,11)
        self.row = 5
        self.column = 7
    


    
    def test_check_block_contain_one_sand_block(self):
        row = 5
        column = 7
        self.game_board.get_board()[row][column]  = 1
        self.assertEquals(self.game_board.check_block(row,column),True)
    




if __name__ == '__main__':
    unittest.main()