import sys
import os
#sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


'''
    Place nime inside the given map mine[index] = '1'
    If there is amine at the given index an RuntimeErro is raise .
'''
def place_mine(mine_map,index):
    # print('util / before / mine_map -> ',mine_map)
    if mine_map[index] == "1":
        raise RuntimeErro
    mine_map = mine_map[:index] + "1" + mine_map[index + 1:]
    # print('util / after / mine_map -> ',mine_map,'(update index 3)')
    return mine_map
    
    #mine_map[index] = "1"
    



'''
@param  (str) - mine_map 
Check if the mine map is free of mine, then return True
else return false.
'''
def map_status(mine_map):
    for cell in mine_map:
        if cell == '1':
            return False
    return True   



def manual_activation(mine_map,index):
    pass



def manual_activation(mine_map):
    pass


