import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_5.solution import PuzzleSolution




class TestCheckBlock(unittest.TestCase):


    

    


    
    def test_check_block_contain_one_sand_block(self):
        row = 5
        column = 7
        game_board = PuzzleSolution(9,11)
        game_board.get_board()[row][column]  = 1
        self.assertEquals(game_board.check_block(row,column),True)




if __name__ == '__main__':
    unittest.main()