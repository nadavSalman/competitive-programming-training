
A_SIZE = 4
B_SIZE = 2*A_SIZE - 1

l = []

def define_ab():
    '''enter 0 to a before you initiate... a[0,...] '''
    a = [0,0,3,6,7]
    b = [0] * (B_SIZE +1)
    for i in range(1,A_SIZE+1):
        b[2*i - 1] = a[i]
        
    return a,b


def xor_a(a):

     sum = a[0]
     for i in range(1,len(a)):
        sum ^= a[i]
     if sum == 0:
         return 1
     else:
         return 0
     

def options(a):
    '''return list of all passable options in range a[i] --> a[i+1]
    for example between 4 to 6 there i 3 options --> 4, 5, 6 '''
    options = []
    for i in range(1,A_SIZE):
        options.append(a[i+1] - a[i] +1)
    print(options)
    return options
     

def create_sequnce(a, options):
    '''for 4 6 7 is [[4,6,7], [6,7]]'''
    sequnces = []
    for i in range(0,len(options)):
        sequnce = []
        for j in range(0,options[i]):
            sequnce.append(a[i+1] + j)
        sequnces.append(sequnce)
    print(sequnces,2) 
    return sequnces
    
def sort_zogi_e_zogi(sequnces):

    l_zogi = []
    l_e_zogi = []
   

    for item in sequnces:
    
        l_s_zogi = []
        l_s_e_zogi = []
   
        for i in range(0,len(item)):
            if item[i]%2 == 0:
                l_s_zogi.append(item[i])
            else:
                l_s_e_zogi.append(item[i])
                
        l_e_zogi.append(l_s_e_zogi)
        l_zogi.append(l_s_zogi)
        
    print(l_e_zogi,'\n',l_zogi)
    return l_zogi, l_e_zogi

def merge(a,b):
    print(a)
    l_merge = []
    for i in range(1,len(a)):
        l_merge.append([a[i]])
        if i < len(a)-1:
            l_merge.append(b[i-1])
    print(l_merge)
    return l_merge

def tree(b_list,empty_list,row,col,l):
    '''run all the the option and check if its 0 if it is count'''
    empty_list.append(b_list[row][col])
    
    if row == len(b_list) - 1:
        #print(empty_list)
        if xor_a(empty_list):
            l.append(xor_a(empty_list))

    else:
        for i in range(0,len(b_list[row+1])):
            tree(b_list, empty_list, row+1, i, l)
            del empty_list[-1]


def main():
    a,b = define_ab()

    xor_a(a)
    sequnces = create_sequnce(a, options(a))
    x = merge(a,sequnces)
    
    l = []
    l2 = []
    cnt = 0
    cnt = tree(x,l,0,0,l2)
    print('the answer is : ',len(l2))

if __name__ == "__main__":
    main()
