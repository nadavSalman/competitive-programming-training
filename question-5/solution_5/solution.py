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
        #self.extract_sand_cells()#not get colled from the constructor
        self.permutation_list = []
        #self.init_permutation(0)

    def get_board(self):
        return self.board.get_boad()

    def get_extracted(self):
        return self.extracted

    def get_scaned_blocks(self):
        return self.scaned_blocks
    
    def get_permutation_list(self):
        return self.permutation_list

    '''
    Perform a check on the given coordinate. 
    If there is block of sand under it disturbed it forward. 
    The disturbed continue recursively until we reach to an empty cell.
    @param : 
        - coordinate - a tuple with two integers.
    '''
    def update_state(self,coordinate,board_copy):
        pass


    def cell_activate(self,coordinate,board_copy):
        pass
        

        




    
    
    def calculate_path(self,cordinates_list,board_copy):
        pass
        #for index in cordinates_list:
       
    
    

    def solve_puzzle(self):
        min_path = None
        count = 0
        for cordinates in self.get_permutation_list():
            print(cordinates)

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
    
    def init_permutation(self,index):
        if index < len(self.extracted):
            for i in range(index ,len(self.extracted)):         
                self.extracted[i] , self.extracted[index] = self.extracted[index] , self.extracted[i] 
                self.init_permutation(index + 1)
                #print(self.permutation_list)
                self.extracted[i] , self.extracted[index] = self.extracted[index] , self.extracted[i] 
        else:
            self.permutation_list.append(self.extracted.copy())       

def main():
    print('solution 5 \n\n')
    
    game = PuzzleSolution(9,11)
    game.get_board()[7][6]  = 1
    game.get_board()[3][8]  = 1
    game.get_board()[4][2]  = 1
    print(game.get_board()," \n") 
    game.extract_sand_cells()
    print('extracted sand cells : \n', game.get_extracted(),"\n")
    game.init_permutation(0)
    print("all extracted sand cells permutation : \n", game.get_permutation_list(),"\n")
    print()
    game.solve_puzzle()

    
if __name__ == "__main__":
    main()