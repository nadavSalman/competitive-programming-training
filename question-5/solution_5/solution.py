import numpy
import sys
import os
from puzzle_board  import PuzzleBoard
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.



class PuzzleSolution(object):
    """docstring for Ciper.
    A cell with the value :  0 - empy , 1 - is blocks of sand.
    """


    def __init__(self,n_rows,m_columns):
        self.board = PuzzleBoard(int,n_rows,m_columns)
        #self.scaned_blocks = self.scan_sand_blocks()

    def get_board(self):
        return self.board.get_boad()

    '''
    Perform a check on the given coordinate. 
    If there is block of sand under it disturbed it forward. 
    The prices continue recursively until we reach to an empty cell.
    @param : 
        - coordinate - a tuple with two integers.
    '''
    def update_state(self,coordinate):
        pass

    def scan_sand_blocks(self):
        for row in self.get_board():
            for cell in row:
                print(cell)




    '''
    Return true if the (i -> row ,j-> column) is blocks of sand, it not return false.
    '''
    def check_block(self,i,j):
        return self.board.get_boad()[i][j] == 1


    '''
    Conver to lmbde / list comperhention expression 
    '''
    def extract_sand_cells(self):
        extracted_cells = []
        for row in range(0,len(self.board.get_boad())):
          for col in range(0,len(self.board.get_boad())):
              if self.check_block(row,col):
                extracted_cells.append((row,col))
        return extracted_cells
                

            



        


def main():
    print('solution 5')
    
    game = PuzzleSolution(9,11)
    game.get_board()[7][6]  = 1
    game.get_board()[3][8]  = 1
    game.get_board()[4][2]  = 1
    extracted_celles = game.extract_sand_cells()
    print(extracted_celles)
   
    
if __name__ == "__main__":
    main()