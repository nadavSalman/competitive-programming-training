import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
class PuzzleBoard(object):
    """Describe a general puzzel"""


    def __init__(self, board_cells_types,n_rows,m_columns):
        self.board_cells_types = board_cells_types #feature stull deeactivate 
        self.n_rows = n_rows
        self.m_columns = m_columns
        self.board = np.zeros((self.n_rows,self.m_columns)).astype(int)


    
    '''
    A get by a board by-reff 
    '''
    def get_boad(self):
        return self.board

    '''
    A get a board by-value 
    '''
    def get_board_copy(self):
        return self.board.copy()


    def __str__(self) -> str:
        #return super().__str__()
        return "PuzzleBoard object data : {} {} {}".format(self.board_cells_types,self.n_rows,self.m_columns)




