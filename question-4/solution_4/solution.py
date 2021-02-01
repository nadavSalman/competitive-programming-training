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

def kuku_solution():
    print('Kuku!!!')
    return 1


'''

'''



def place_mine(mine_map,index):
    #print('util / before / mine_map -> ',mine_map)
    if mine_map[index] == "1":
        raise RuntimeErro
    mine_map = mine_map[:index] + "1" + mine_map[index + 1:]
    #print('util / after / mine_map -> ',mine_map,'(update index 3)')
    return mine_map


def main():
    print('solution-4')

if __name__ == "__main__":
    main()