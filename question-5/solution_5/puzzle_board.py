import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
class PuzzleBoard(object):
    """Describe a general puzzel"""


    def __init__(self, board_cells_types,n_rows,m_columns):
        self.board_cells_types = board_cells_types #feature stull deeactivate 
        self.board_height = n_rows
        self.board_width = m_columns
        self.board = np.zeros((self.board_height,self.board_width)).astype(int)
    



    
    '''
    A get by a board by-reff 
    '''
    def get_board(self):
        return self.board

    '''
    A get a board by-value 
    '''
    def get_board_copy(self):
        return self.board.copy()


    def __str__(self):
        #return super().__str__()
        return "PuzzleBoard object data : {} {} {}".format(self.board_cells_types,self.n_rows,self.m_columns)




