import sys
import os

from util import place_mine , map_status , manual_activation , manual_activation_v2 ,place_mine_list

class Ciper(object):
    """docstring for Ciper."""


    def __init__(self, mine_map):
        # super(Ciper, self).__init__()
        self.mine_map = mine_map



    def ciper_job(self,mine_map,index,manual_activation_price,place_mine_price):
        if map_status(mine_map):
            #recurtion break
            return 0
        if index < mine_map.__len__():
            #check if ther is a mine:
            if mine_map[index] == '1':
                mine_before_activation = mine_map.copy()
                manual_activation(mine_map,index)
                return min(self.ciper_job(mine_map,index + 1,manual_activation_price,place_mine_price) + manual_activation_price,
                            self.ciper_job(mine_before_activation,index + 1,manual_activation_price,place_mine_price))
            else:#If there is no mine
                #place a mine under a building , or do nathing.
                mine_before_pacing = mine_map.copy()
                place_mine_list(mine_map,index)
                return min(self.ciper_job(mine_map,index + 1,manual_activation_price,place_mine_price) + place_mine_price,
                            self.ciper_job(mine_before_pacing,index + 1,manual_activation_price,place_mine_price))
        else:
            #recurtion break
            return mine_map.__len__() * manual_activation_price + mine_map.__len__() * place_mine_price # return max value to make shure the sequence of operation will not count as  the minimum number of coins that the sapper will have to pay.

    def solve(self,manual_activation_price,place_mine_price):
        return self.ciper_job(self.mine_map,0,manual_activation_price,place_mine_price)
