import sys
import os

import sys
import os
#In order to run as stand alone scriot : main == name ....
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)#Add to path parent dir.
'''
os.path.dirname(os.path.realpath('test_swap_by_prefix.py'))
->'/home/nadav/competitive-programming-training/question-2/tests'
os.path.dirname(os.path.dirname(os.path.realpath('test_swap_by_prefix.py')))
->'/home/nadav/competitive-programming-training/question-2'
>>> 
'''
from util import place_mine , map_status , manual_activation




def ciper_job(mine_map,index,manual_activation_price,place_mine_price):
    if map_status(mine_map):
        return 0
    if index < mine_map.__len__():
        #check if ther is a mine:
        if mine_map[index] == '1':
            #manual activation of the mine.
            mine_map = manual_activation(mine_map,index)

        else:#If there is no mine
            #place a mine under a building.
            mine_map = place_mine(mine_map,index)


    else:
        return mine_map.__len__() * manual_activation_price + mine_map.__len__() * place_mine_price # return max value to make shure the sequence of operation will not count as  the minimum number of coins that the sapper will have to pay.


    
    



def solve():
    pass

def main():
    print('solution-4')

if __name__ == "__main__":
    main()