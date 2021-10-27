import numpy
import sys
import os
from solution_5.puzzle_board  import PuzzleBoard
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.



class PuzzleSolution(object):
    """docstring for Ciper.
    A cell with the value :  0 - empy , 1 - is blocks of sand.
    """


    def __init__(self,n_rows,m_columns):
        self.board = PuzzleBoard(int,n_rows,m_columns)

    def get_board(self):
        return self.board.get_boad()

    '''
    Perform a check on the given coordinate. 
    If there is block of sand under it disturbed it forward. 
    The prices continue recursively until we reach to an empty cell.
    '''
    def update_state(self,coordinate):
        pass



    '''
    Return true if the (i -> row ,j-> column) is blocks of sand, it not return false.
    '''
    def check_block(self,i,j):
        return self.board.get_boad()[i][j] == 1

        


def main():
    print('solution 5')
    game = PuzzleSolution(9,11)
    game.get_board()[7][6]  = 1
    game.get_board()[3][8]  = 1
    game.get_board()[4][2]  = 1
    print(game.get_board()) 
    print(game.check_block(7,3))  
  
    
if __name__ == "__main__":
    main()