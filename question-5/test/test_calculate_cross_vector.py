import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from solution_5.solution import PuzzleSolution



class TestCalculateCrossVector(unittest.TestCase):


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
    def test_calculate_cross_vector_point_in_the_middle(self):
        rows = 3
        columns = 4
        game_board = PuzzleSolution(rows,columns)
        cordinates_test = (1,1) # (row,col)
        calculate_vector = game_board.calculate_cross_vector(cordinates_test)
        expected_vector = {   'down': [(2,1)],'left': [(1,0)],'right': [(1,2),(1,3)],'up': [(0,1)]  }
        self.assertEqual(calculate_vector,expected_vector)

        
    def test_calculate_cross_vector_point_in_the_curnner(self):
        rows = 3
        columns = 4
        game_board = PuzzleSolution(rows,columns)
        cordinates_test = (2,1) # (row,col)
        calculate_vector = game_board.calculate_cross_vector(cordinates_test)
        expected_vector = {   'down': [],'left': [(2,0)],'right': [(2,2),(2,3)],'up': [(1,1),(0,1)]  }
        self.assertEqual(calculate_vector,expected_vector)

        


if __name__ == '__main__':
    unittest.main()