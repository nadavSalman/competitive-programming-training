<<<<<<< HEAD
import random
import math

M = 5
N = 5
R = 10

def input():

    l = []
    
    for i in range(0,N):
        l_sub = []
        for j in range(0,M):
            rand = random.randint(0,9)
            l_sub.append(rand)       
        l.append(l_sub)
        print(l_sub, '\n')
   
    return l
    
def radius_0():
    
    l = input()
    max_1 = 0
    max_2 = 0
    
    for i in range(0,N):
        for j in range(0,M):

            if l[i][j] > max_1:
                max_1 = l[i][j]
            
            elif l[i][j] > max_2:
                max_2 = l[i][j]

    sum = max_1 + max_2
    
    cnt_max_1 = 0
    cnt_max_2 = 0
    for i in range(0,N):
        cnt_max_1 += l[i].count(max_1)
        cnt_max_2 += l[i].count(max_2)
    
    number_of_options = cnt_max_1 * cnt_max_2

    print(" sum: " , sum , " number of options:", number_of_options )

def find_outside_circle_point(i = 0, j = 0):

    """this methed return list of all y value of the hafe circle
    """

    y = []

    for x in range(i, 2*R):
        #R^2 = (x-a)^2 + (y-b)^2
        #R^2 - (x-a)^2 = (y-b)^2
        # /--------------|                      
        #V R^2 - (x-a)^2   = (y-b)
        # /--------------|                      
        #V R^2 - (x-a)^2   - b = y
        
        # for [0,0]cricle only
        a = i + R
        b = j + R
        # center [a,b]
        #R = 2
        #y = ?
        answer = math.sqrt(R**2 - (x-a)**2) - b
        answer = abs(answer)
        answer = round(answer + 0.5)
        y.append(answer)
   
    print(y) 
    
def sum_circle(y_list, rand_num_list):
    sum = 0
    for i in range(0, len(y_list))
        for j in range(y_list[i], R-y_list[i]):
           sum +=  rand_num_list[i][j]
    

def circle_index():
        l = input()
        for i in range(0,N):
            if i+(R*2) < N:             # if the list can contain koter cricle that big (horizontal)
                for j in range(0,M):
                    if i+(R*2) < N:     # if the list can contain koter cricle that big (vetical)
                        print('')
            
    
    

def main():
    find_outside_circle_point()    
    
if __name__ == "__main__":
    main()
=======
print('hi there question 1')
print('kukuriku')
>>>>>>> e044eba5b30217dca55bc948334709722c5aea12
