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
        """Calculate all cross vectors from the given coordinate (row,col) to the edge of the board
        Args:
            The scanning isnt in the netural form ofcartesian cordinate system.
            Keep in maind instead of the origin placed in the mosdown left curner it placed in the most left up curner.
            coordinates (Tuple): (row,col) coordinates.
            A -> (0,0) Z -> (board_height - 1,board_height -1)
           [[A 0 0 0 0 0 * 0 0 0 Z]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [* * * * * * * * * * *]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]
            [0 0 0 0 0 0 * 0 0 0 0]]
        """
        # A cartesian cordinate system solution :
        # x , y = coordinates[0] , coordinates[1]
        # return  {   # v - vector to the board edge 
        #     'up' : [(x,v) for v in range(y+1,self.board.board_height,1)],
        #     'down' : [(x,v) for v in range(y-1,-1,-1)],
        #     'right': [(v,y) for v  in range(x+1,self.board.board_width,1)],
        #     'left': [(v,y) for v in range(x-1,-1,-1)]
        # }  
        
        row , col = coordinates[0] , coordinates[1]
        return  {   # v - vector to the board edge 
            'up' : [(v,col) for v in range(row - 1,-1,-1)],
            'down' : [(v,col) for v in range(row - 1,self.board.board_height,-1)], 
            'right': [(row,v) for v in range(col + 1,self.board.board_width,1)],
            'left': [(row,v) for v in range(col - 1,-1,-1)]
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
        """Scan for sand cell by row and column.
        """
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
    
    def delete_sand_sell(self,cordinates):
        self.get_board()[cordinates[0]][cordinates[1]] = 0

    def activate_permutaion(self,permutation_list,index):
        """activate the alist of permutaion on a board.
           Return (int) the number of steps.
        Args:
            permutation_list ([list]): sand cells too activate
        """
        if index < len(permutation_list):
            x = permutation_list[index][0] , y = permutation_list[index][1]
            self.board[x][y] = 0 # activate current cell .
            #chain_reaction(...)
            # return 1 + activate_permutaion 
        return 0

    def chain_reaction(self,permutation_list,index):
        self.delete_sand_sell(permutation_list[index])#update board state
        # Disturbed the given block of sand forward. 
        cross_vectors = self.calculate_cross_vector(permutation_list[index])
        print('cross vectors for cordinate : ',permutation_list[index],' vectors \n         ->',cross_vectors)
        permutation_list = self.delet_list_elemet(permutation_list,index) # remove the current activate cell cordinate from the permutation list.
        for key  in cross_vectors:
            for cordinate in cross_vectors[key]:
                if cordinate in permutation_list:
                    cordinate_index = permutation_list.index(cordinate)# calculate the index to remve.
                    self.chain_reaction(permutation_list,cordinate_index)

    def delet_list_elemet(self,list,index):
        return list[0:index] + list[index+1:len(list)]
   
    def conver_cartesian_to_board_access_point(self,cordinates):
        print('board_height : ',self.board.board_height)
        print('board_width : ',self.board.board_width)
        return (self.board.board_height - cordinates[0],self.board.board_height - cordinates[1])
        
def main():
    print('solution 5 \n\n')
    
    game = PuzzleSolution(9,11)
    # Fill cells with sand
    game.get_board()[7][6]  = 1
    game.get_board()[3][6]  = 1
    game.get_board()[3][2]  = 1
    game.get_board()[8][10]  = 1
    game.init_permutation(0)
    print('source board :\n',game.get_board()," \n") 

    print(game.conver_cartesian_to_board_access_point((0,10)))   
    
    
    
    
    
        
    # cross_vectors = game.calculate_cross_vector((3,3))
    # for key in cross_vectors:
    #     print(key)
 
    #game.chain_reaction([(7,6),(3,6),(4,2)],0)

    #print('source board after chain reaction :\n',game.get_board()," \n") 
    
    
    
    #copy_match = PuzzleSolution(9,11)
    #copy_match.set_board(game.get_board_copy())
    #copy_match.get_board()[4][2]  = 0
    #print('copy match : ',copy_match.get_board()," \n") 
    # game.extract_sand_cells()
    # print('extracted sand cells : \n', game.get_extracted(),"\n")
    
    # print("all extracted sand cells permutation : \n", game.get_permutation_list(),"\n")
    # print()

    
if __name__ == "__main__":
    main()