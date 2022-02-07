from audioop import cross
from multiprocessing.dummy import active_children
from traceback import print_tb
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
        self.current_list = []
        

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
            'down' : [(v,col) for v in range(row + 1,self.board.board_height,1)], 
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

    def extract_sand_cells(self):
        """Scan for sand cell by row and column.
        """
        extracted_cells = []
        for row in range(0,self.board.board_height):
          for col in range(0,self.board.board_width):
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
        
    def set_current_list(self,list):
        self.current_list = list
        
    def activate_permutaion_beta(self,index):
            """activate the alist of permutaion on a board.
            Return (int) the number of steps.
            Args:
                permutation_list ([list]): sand cells too activate
            """
            if index < len(self.current_list) : # if permutation_list isn't empty
                if self.current_list[index] == (-1,-1):
                    return self.activate_permutaion_beta(index + 1) 
                else:
                    self.chain_reaction_beta(index) # update permutation_list by passing it with ref.
                    return 1 +  self.activate_permutaion_beta(index + 1) 
            return 0
    
    def chain_reaction_beta(self,index):
        """Disturbed the given block of sand forward.
        Args:
            self.current_list ([(row,col)]): [description]
            index integer : [description]
        """
        if index < len(self.current_list):
            self.delete_sand_sell(self.current_list[index]) #update board state
            cross_vectors = self.calculate_cross_vector(self.current_list[index]) # Disturbed the given block of sand forward. 
            self.current_list[index] = (-1,-1)
            for key  in cross_vectors: # run on the cruss vector cordinate, kesy : up, down, left, right.
                for cordinate in cross_vectors[key]:
                    if cordinate in self.current_list:
                        cordinate_index = self.current_list.index(cordinate)# calculate the index to be removed.
                        self.chain_reaction_beta(cordinate_index)
        
        
        

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
    game.get_board()[0][0]  = 1
    game.get_board()[7][6]  = 1
    game.get_board()[3][6]  = 1
    game.get_board()[3][10]  = 1
    game.get_board()[0][10]  = 1
    game.get_board()[3][2]  = 1
    game.get_board()[8][10]  = 1
    game.get_board()[5][4]  = 1
    game.get_board()[5][0]  = 1
    
    print('source board :\n',game.get_board()," \n") 
    
    game.extract_sand_cells()
    print(f'game.get_extracted() -> \n  {game.get_extracted()} \n')
    
    game.init_permutation(0)    
    
    permutation_test = [(7,6),(5,4),(3,6),(5,0),(3,2),(0,0),(8,10),(0,10),(3,10)]
    if permutation_test in game.get_permutation_list():
        print('yes')
        index = game.get_permutation_list().index(permutation_test)
        print(index)
        print(game.get_permutation_list()[index])
        
    valid_permutation = game.get_permutation_list()[index]
    game.set_current_list(valid_permutation)
    print(f'activate_permutaion_beta -> {game.activate_permutaion_beta(0)}')
    print('Current list after selected point activation  : ',game.current_list)
    
    print('Post actions board state :\n',game.get_board()," \n") 
    
    
    
    
    #print(game.activate_permutaion_beta(,0))
    
    
    #print(game.activate_permutaion(permutation_test,0))
    
    # print('Start chain reaction on : ',permutation_test)
    # game.chain_reaction(permutation_test,0)
    # print('source board :\n',game.get_board()," \n") 

    #print(game.conver_cartesian_to_board_access_point((0,10)))   
    
    
    
    
    
        
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