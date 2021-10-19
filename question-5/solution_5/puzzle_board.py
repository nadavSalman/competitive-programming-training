import numpy as np


class PuzzleBoard(object):
    """docstring for Ciper."""


    def __init__(self, board_cells_types,n_rows,m_columns):
        self.board_cells_types = board_cells_types #feature stull deeactivate 
        self.n_rows = n_rows
        self.m_columns = m_columns
        self.board = np.zeros((self.n_rows,self.m_columns)).astype(int)


    def __str__(self) -> str:
        #return super().__str__()
        return "PuzzleBoard object data : {} {} {}".format(self.board_cells_types,self.n_rows,self.m_columns)


    '''
    A get by reff funciton
    '''
    def get_boad(self):
        return self.board

    '''
    A get by value 
    '''
    def get_board_copy(self):
        pass


