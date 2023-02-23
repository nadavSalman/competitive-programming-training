
# >>> int(bin(1)[2:],2)
# 1
# >>> int(bin(10)[2:],2)
# 10
# >>> bin(110)
# '0b1101110'
# >>> bin(110)[2:]
# '1101110'
# >>> 








def equal_binary_parts(Z):
    # Compute the total number of ones in the input list
    total_ones = sum(Z)

    # If the total number of ones is not divisible by 3, then no solution exists
    if total_ones % 3 != 0:
        return None

    # Compute the number of ones that should be present in each part
    ones_per_part = total_ones // 3

    # Initialize counters for the number of ones seen so far and the current part number
    ones_seen = 0
    part_num = 0

    # Iterate over the input list to find the indices that separate the three parts
    i, j = None, None
    for idx, val in enumerate(Z):
        ones_seen += val
        if ones_seen == ones_per_part * (part_num + 1):
            if part_num == 0:
                i = idx
            elif part_num == 1:
                j = idx
            part_num += 1

    # If we found all three parts, return their indices
    if i is not None and j is not None:
        return [i, j]

    # Otherwise, no solution exists
    return None


        
def main(): 
    z = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
    print(equal_binary_parts(z))


if __name__ == "__main__":
    main()