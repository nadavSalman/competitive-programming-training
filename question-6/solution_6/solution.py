

def transform_into_non_increasing(l):
    operation_count = 0
    for index in range(0, len(l)-1):
        pivot = index
        operation_count += recursive_back_rolling(l,pivot,operation_count)
    return operation_count

def recursive_back_rolling(dishes,index,operation_count):
    if index > -1:
        if not dishes[index] >= dishes[index+1]:
            dishes[index] += 1
            dishes[index + 1] -= 1
            operation_count += 2
            recursive_back_rolling(dishes,index,operation_count)
        recursive_back_rolling(dishes,index - 1,operation_count)
    return operation_count
            
        
def main():
    input_array = [1, 2, 5, 6, 7, 4]
    transform_into_non_increasing(input_array)
    print(input_array)


if __name__ == "__main__":
    main()
