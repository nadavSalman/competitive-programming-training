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
        #self.extracted  = self.extract_sand_cells()
        self.extracted = []
        self.extract_sand_cells()

    def get_board(self):
        return self.board.get_boad()


    def get_scaned_blocks(self):
        return self.scaned_blocks

    '''
    Perform a check on the given coordinate. 
    If there is block of sand under it disturbed it forward. 
    The prices continue recursively until we reach to an empty cell.
    @param : 
        - coordinate - a tuple with two integers.
    '''
    def update_state(self,coordinate):
        pass




    '''
    def solve_puzzel(self,index):
        if index < len(sand_cells):
            if all_send_cells_activated(index) 
    '''

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
        #return extracted_cells
        self.extracted = extracted_cells
                

            
extornal_storage = []

def permutation(array,index):
    if index < len(array):
        for i in range(index ,len(array)):         
            array[i] , array[index] = array[index] , array[i] 
            permutation(array.copy(),index + 1)
            array[i] , array[index] = array[index] , array[i] 
    else:
        print(array)


    


        


def main():
    print('solution 5')
    permutation([1,2,3],0)
    print(extornal_storage)
    
    '''
    game = PuzzleSolution(9,11)
    game.get_board()[7][6]  = 1
    game.get_board()[3][8]  = 1
    game.get_board()[4][2]  = 1
    print(game.get_board())
    game.extract_sand_cells()
    print(game.extracted)
    '''
    
if __name__ == "__main__":
    main()