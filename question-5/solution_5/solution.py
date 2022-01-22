from audioop import cross
import numpy
import sys
import os

import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
#from puzzle_board import PuzzleBoard
from solution_5.puzzle_board import PuzzleBoard


class PuzzleSolution(object):
    """docstring for Ciper.
    A cell with the value :  0 - empy , 1 - is blocks of sand.
    """
    def __init__(self,n_rows,m_columns):
        self.board = PuzzleBoard(int,n_rows,m_columns)
        self.extracted = []
        self.permutation_list = []

    def get_board(self):
        return self.board.get_board()
    
    def get_board_copy(self):
        return self.board.get_board().copy()
    
    def set_board(self,new_board):
        self.board.set_board(new_board)

    def get_extracted(self):        
        return self.extracted

    def get_scaned_blocks(self):
        return self.scaned_blocks
    
    def get_permutation_list(self):
        return self.permutation_list
        
    def calculate_cross_vector(self,coordinates):
        """Calculate all cross vectors from the given coordinate to the edge of the board
        Args:
            coordinates (Tuple): (row,col) coordinates.
            A - (0,0) Z - (board_height - 1,board_height -1)
            [0 0 0 0 0 0 * 0 0 0 Z]
           [[0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [* * * * * * * * * * *]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [A 0 0 0 0 0 * 0 0 0 0]]
        """
        x , y = coordinates[0] , coordinates[1]
        return  {   # v - vector to the board edge 
            'up' : [(x,v) for v in range(y+1,self.board.board_height,1)],
            'down' : [(x,v) for v in range(y-1,-1,-1)],
            'right': [(v,y) for v  in range(x+1,self.board.board_width,1)],
            'left': [(v,y) for v in range(x-1,-1,-1)]
        }  
    
    def calculate_path(self,cordinates_list,board_copy,minimum,index,counter):
        if index < len(cordinates_list):
            # activate the i cell
            row , col = cordinates_list[index][0] , cordinates_list[index][1]

    def solve_puzzle(self):
        min_path = None
        count = 0
        for cordinates in self.get_permutation_list():
            print(cordinates)

    def check_block(self,i,j):
        return self.board.get_board()[i][j] == 1

    '''
        *Conver to lmbde / list comperhention expression 
    '''
    def extract_sand_cells(self):
        extracted_cells = []
        for row in range(0,len(self.board.get_board())):
          for col in range(0,len(self.board.get_board())):
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

    def activate_permutaion(self,permutation_list,index):
        """activate the alist of permutaion on a board.
           Return (int) the number of steps.
        Args:
            permutation_list ([list]): sand cells too activate
        """
        if index < len(permutation_list):
            x = permutation_list[index][0] , y = permutation_list[index][1]
            self.board[x][y] = 0 # activate current cell .
            # Disturbed the given block of sand forward. 
            cross_vectors = self.calculate_cross_vector(permutation_list[index])
            
            
            
            

def update_state(self,coordinate,source_board,cordinates_list):
    """Disturbed the given block of sand forward. 
    The disturbed continue recursively until we reach to an empty cell. 

    Args:
        coordinate ([Tuple]): (X,Y) 
        source_board ([Two d list]): 
        cordinates_list
    """



def main():
    print('solution 5 \n\n')
    
    game = PuzzleSolution(9,11)
    # Fill cells with sand
    game.get_board()[7][6]  = 1
    game.get_board()[3][8]  = 1
    game.get_board()[4][2]  = 1
    copy_match = PuzzleSolution(9,11)
    copy_match.set_board(game.get_board_copy())
    copy_match.get_board()[4][2]  = 0
    print('copy match : ',copy_match.get_board()," \n") 
    print('source board : ',game.get_board()," \n") 
    
    # game.extract_sand_cells()
    # print('extracted sand cells : \n', game.get_extracted(),"\n")
    # game.init_permutation(0)
    # print("all extracted sand cells permutation : \n", game.get_permutation_list(),"\n")
    # print()

    
if __name__ == "__main__":
    main()