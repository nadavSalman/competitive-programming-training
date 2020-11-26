
A_SIZE = 3
B_SIZE = 2*A_SIZE - 1


def define_ab():
    
    a = [0,4,6,7]
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
    
    

 
def condition():
    # the list sum need to be equal to a sum
    #
    print("hello")



def main():
    a,b = define_ab()
    xor_a(a)
    create_sequnce(a, options(a))

if __name__ == "__main__":
    main()