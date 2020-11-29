
A_SIZE = 3
B_SIZE = 2*A_SIZE - 1


def define_ab():
    
    a = [0,0,1,3]
    b = [0] * (B_SIZE +1)
    
    for i in range(1,A_SIZE+1):
        b[2*i - 1] = a[i]
        
    return a,b

def xor_a(a):

     sum = a[1]
     for i in range(2,A_SIZE +1):
        sum ^= a[i]
     
     print(sum)
     return sum
     
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
    print(sequnces) 
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


 
def condition():
    # the list sum need to be equal to a sum
    #
    print("hello")



def main():
    a,b = define_ab()
    xor_a(a)
    sequnces = create_sequnce(a, options(a))
    
    zogi, e_zogi = sort_zogi_e_zogi(sequnces)
   

if __name__ == "__main__":
    main()