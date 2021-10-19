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
    nadav_board.get_boad()[5][6] = 1
    print(nadav_board.get_boad())



    




if __name__ == "__main__":
    main()