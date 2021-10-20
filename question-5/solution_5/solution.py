import numpy
from puzzle_board import PuzzleBoard




def main():
    print('solution 5')
    
    '''
    Generate matrix of type int :
        [[0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0]
        [0 0 0 0 0 0 0]]
    '''
    zeors_array = numpy.zeros((5,7)).astype(int)
    #print(zeors_array)
    nadav_board = PuzzleBoard(int,6,9)
    print(nadav_board)
    new_board = nadav_board.get_boad().copy()
    new_board[1][4] = 8
    print(nadav_board.get_boad())
    print("new board : ")
    print(new_board)



    




if __name__ == "__main__":
    main()