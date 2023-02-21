
# >>> int(bin(1)[2:],2)
# 1
# >>> int(bin(10)[2:],2)
# 10
# >>> bin(110)
# '0b1101110'
# >>> bin(110)[2:]
# '1101110'
# >>> 

def equal_sub_binary(dec_value,power,binary_input):
    groups_count = 0
    sub_binary = ''
    for index in range(0,binary_input):
        if binary_input[index] == '1':
            sub_binary += '1'
            if int(sub_binary) ==  dec_value:
                groups_count += 1
                 



        


def main():
    print('sdfsd')

if __name__ == "__main__":
    main()