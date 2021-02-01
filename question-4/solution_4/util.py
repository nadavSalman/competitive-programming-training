import sys
import os
#sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))



def place_mine(mine_map,index):
    print('util / before / mine_map -> ',mine_map)
    if mine_map[index] == "1":
        raise RuntimeErro
    mine_map = mine_map[:index] + "1" + mine_map[index + 1:]
    print('util / after / mine_map -> ',mine_map,'(update index 3)')
    return mine_map
    
    #mine_map[index] = "1"
    


def manual_activation(mine_map):
    pass


