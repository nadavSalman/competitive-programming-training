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
from util import place_mine , map_status , manual_activation , manual_activation_v2 ,place_mine_list

from ciper import Ciper







#coins_to_pay
def ciper_job(mine_map,index,manual_activation_price,place_mine_price):
    if map_status(mine_map):
        #recurtion break
        return 0
    if index < mine_map.__len__():
        #check if ther is a mine:
        if mine_map[index] == '1':
            mine_before_activation = mine_map.copy()
            manual_activation(mine_map,index)
            return min(ciper_job(mine_map,index + 1,manual_activation_price,place_mine_price) + manual_activation_price,
                        ciper_job(mine_before_activation,index + 1,manual_activation_price,place_mine_price))
        else:#If there is no mine
            #place a mine under a building , or do nathing.
            mine_before_pacing = mine_map.copy()
            place_mine_list(mine_map,index)
            return min(ciper_job(mine_map,index + 1,manual_activation_price,place_mine_price) + place_mine_price,
                        ciper_job(mine_before_pacing,index + 1,manual_activation_price,place_mine_price))
    else:
        #recurtion break
        return mine_map.__len__() * manual_activation_price + mine_map.__len__() * place_mine_price # return max value to make shure the sequence of operation will not count as  the minimum number of coins that the sapper will have to pay.







def solve():
    pass

def main():


    print('solution-4~')
    ciper = Ciper(['0','1','0','0','0','0','1','0'])
    print(ciper.solve(1,1))
    #01000010
    # print(ciper_job(['0','1','0','0','0','0','1','0'],0,1,1))
    #print(manual_activation_v2("0111",2))

if __name__ == "__main__":
    main()
