import sys
import os
#sys.path.append(os.getcwd()+'/question2/solution')#to allaw import solution model (nat the best way ...)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


'''
    Place nime inside the given map mine[index] = '1'
    If there is amine at the given index an RuntimeErro is raise .
    Treat the nime map as string.
'''
def place_mine(mine_map,index):
    # print('util / before / mine_map -> ',mine_map)
    if mine_map[index] == "1":
        raise RuntimeErro
    mine_map = mine_map[:index] + "1" + mine_map[index + 1:]
    # print('util / after / mine_map -> ',mine_map,'(update index 3)')
    return mine_map

    #mine_map[index] = "1"



def place_mine_list(mine_map,index):
    mine_map[index] = '1'

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




'''
active mine at the index location.
When a mine under the building numbered x is activated,
it explodes and activates two adjacent mines under the buildings numbered x−1 and x+1
if there were no mines under the building, then nothing happens.


Example :
for the given mine_map = "1011010" , index = 2:
the outcame manual_activation(mine_map,index) will produce the blow sequesnce of operation.

-> active cell at index 3 -> "101*010" -> "10**010" ->  mine_map = "1000010"


the parameter mine_map is pass by ref.

sence str in imutable object , we cant use it as ref param . so the map will be converted to lis .

Tracking :

map = '10110'
                        mc(map,3)
                        map -> '10100'
                        /             \
                mc(map,2)              mc(map,4)
            map -> '10000'               out.
           /             \
    mc(map,1)       mc(map,3)
       out            out
'''
def manual_activation(mine_map,index):
    if index >=0 and index < mine_map.__len__():
        if mine_map[index] == '1':
            mine_map[index] = '0'#active mine at index .
            manual_activation(mine_map,index + 1)
            manual_activation(mine_map,index - 1)



# mine_map str param.
def manual_activation_v2(mine_map,index):
    if index >=0 and index < len(mine_map):
        if mine_map[index] == '1':
            mine_map = mine_map[:index] + "0" + mine_map[index + 1:]#transfer digit at index from 1 to 0.
            new_mine_map = manual_activation_v2(mine_map,index + 1)
            new_mine_map = manual_activation_v2(new_mine_map,index - 1)
            return new_mine_map
    return mine_map







def str_to_list_convert(mine_map_str):
    mine_map_list = []
    for char in mine_map_str:
        mine_map_list.append(char)
    return mine_map_list


def list_to_str_convertor(mine_map_list):
    mine_map_str = ""
    for cell in mine_map_list:
        mine_map_str = mine_map_str[:mine_map_str.__len__()] + str(cell)
    return mine_map_str

def main():
    print('~~~question-4/util.py')

    print(list_to_str_convertor([1,1,1,0,1,0]))


    # mine_map_list = str_to_list_convert('10101001')
    # print(mine_map_list)

    # my_map = '10110'
    # print('my_map before manual activation : ',my_map)
    # manual_activation(my_map,3)
    # print('my_map after  manual_activation(my_map,3) : ',my_map)


if __name__ == "__main__":
    main()
