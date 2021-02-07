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



#coins_to_pay
def ciper_job(mine_map,index,manual_activation_price,place_mine_price):
    if map_status(mine_map):
        return 0
    if index < mine_map.__len__():

        
        #check if ther is a mine:
        if mine_map[index] == '1':
            #manual activation of the mine or do nathing.
            return min(ciper_job(manual_activation(mine_map,index),index,manual_activation_price,place_mine_price) + manual_activation_price,
            ciper_job(manual_activation(mine_map,index),index,manual_activation_price,place_mine_price))
        else:#If there is no mine
            #place a mine under a building , or do nathing.
            return min(ciper_job(manual_activation(mine_map,index),index,manual_activation_price,place_mine_price) + place_mine_price,
            ciper_job(manual_activation(mine_map,index),index,manual_activation_price,place_mine_price))
    else:
        return mine_map.__len__() * manual_activation_price + mine_map.__len__() * place_mine_price # return max value to make shure the sequence of operation will not count as  the minimum number of coins that the sapper will have to pay.


    
    



def solve():
    pass

def main():
    print('solution-4')

if __name__ == "__main__":
    '''
    5 1
    01101110
    '''
    my_mine_map = "01101110"
    print(ciper_job(my_mine_map,0,5,1))
    main()