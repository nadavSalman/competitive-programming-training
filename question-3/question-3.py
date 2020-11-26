
A_SIZE = 5
B_SIZE = 2*A_SIZE - 1


def define_ab():

    
    a = [0,1,4,5,6,18]
    b = [0] * (B_SIZE +1)
    

    for i in range(1,A_SIZE+1):
        b[2*i - 1] = a[i]
        
    return a,b

def xor_equal_0(a):

    # 1 00000
    # 2 00001 e-zogi 
    # 3 00010
    # 4 00011 e-zogi
    # 5 00100
    #
    

    # [1,1,4,4,5,5,6,6,18,18]
    for i in range(0,A_SIZE):
        b[i] = a[i]
    


def xor_b(b):
    
    
    n = b[0]
    for i in range(1,B_SIZE + 1):
        n ^= b[i] 

    return n

def main():
    a,b = define_ab()
    print(a)
    print(b)
    
    print('n:', xor_b([1,1,4,4,5,5,6,6,18,18]))

if __name__ == "__main__":
    main()