import random


def input_random(n = 9, m = 9, r = 1):
    print("\n", n, m, r, end = "\n\n")
    for i in range(0,int(n)):
        for j in range(0,int(m)):
            print(random.randint(0,9), end = " ")
        print("")
         

def main():
    input_random()
    
    
    
    
    
if __name__ == "__main__":
    main()