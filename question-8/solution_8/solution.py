





# Decode String Part 1 

'''
as3rkf2e -> asrrrkfee
'''

def decode_str_part_1(str):
    decode = ''
    index = 0
    num = ''
    while index < len(str):
        if str[index].isnumeric():
            num += str[index]
        elif num != '':
            decode += int(num) * str[index]
            num = ''
        index += 1
    return decode




'''
ab2[c]3[de4[f]] -> abccdeffffdeffffdeffff
2[2[2[a]]] -> aaaaaaaa
Python’s built-in data structure list can be used as a stack.
Stack Push -> my_list.append()
Stack Pop -> my_list.pop()
'''
def decode_atr(str):
    multiple_factors_stack = []
    square_bracket_stack = []
    decode = ""
    idx = 0
    while idx < len(str):
        val = str[idx]
        # print(f"Current index: {idx} , str[idx] -> {val}")
        if (not val.isnumeric()) and val != '[' and val !=  ']':
            if (not square_bracket_stack):
                decode += val
            elif square_bracket_stack:
                if square_bracket_stack[len(square_bracket_stack) -1] == '[':
                    square_bracket_stack.append(val)
                else: 
                    square_bracket_stack[len(square_bracket_stack) -1] += val
        elif val.isnumeric():
            multiple_factors_stack.append(val)
        elif val == '[':
            square_bracket_stack.append(val)
        else: # val == ']':
            multiple_factor = multiple_factors_stack.pop()
            target_val = square_bracket_stack.pop()
            square_bracket_stack.pop() # pop out '['
            new_val = int(multiple_factor) * target_val
            if square_bracket_stack:
                square_bracket_stack[len(square_bracket_stack) -1] += new_val
            else:
                decode += new_val

        idx += 1
    return decode
           


         
       
            


def main():
    # print(decode_atr('ab2[c]3[de4[f]]'))
    inpus = ['ab2[cd]e','ab2[c]3[de4[f]]']
    for input in inpus:
        print(f'Input: {input} , Output:{decode_atr(input)}')

if __name__ == '__main__':
    main()