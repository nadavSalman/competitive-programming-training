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
        self.assertEqual(game_board.check_block(row,column),True)

    '''
    Input :

        2   0 | 0 0
        1   - * - -
        0   0 | 0 0

            0  1  2
    
    Expected Output :
    {   'down': [(0,1)],
        'left': [(1,0)],
        'right': [(1,2),(1,3)],
        'up': [(2,1)]  }
    '''
    def test_calculate_cross_vector(self):
        rows = 3
        columns = 4
        game_board = PuzzleSolution(rows,columns)
        cordinates_test = (1,1)
        calculate_vector = game_board.calculate_cross_vector(cordinates_test)
        expected_vector = {   'down': [(1,0)],'left': [(0,1)],'right': [(2,1),(3,1)],'up': [(1,2)]  }
        self.assertEqual(calculate_vector,expected_vector)

        



if __name__ == '__main__':
    unittest.main()