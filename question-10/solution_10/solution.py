def binary_trim_prefix(array,index = 0):    
    if array[index] == 1:
        return array
    else:
        return binary_trim_prefix(array[index+1:])

def partition_devider(partition_i, partition_j,input_array):
    partition_a = input_array[0:partition_i + 1]
    partition_b = input_array[partition_i + 1:partition_j]
    partition_c = input_array[partition_j:len(input_array)]
    # print(f'Partition dediver  \n  0 : i ->  {partition_a}\n  i+1 : j-1 -> {partition_b}\n  j : -1 -> {partition_c}')
    return [
        binary_trim_prefix(partition_a, 0),
        binary_trim_prefix(partition_b, 0),
        binary_trim_prefix(partition_c, 0),
    ]

def binary_equality(partition_i, partition_j,input_array):
    # print(f"partition_i: {partition_i}, partition_j: {partition_j}, input_array: {input_array}")
    binary_partitions = partition_devider(partition_i, partition_j,input_array)
    # print(f"binary_partitions: {binary_partitions}")
    return binary_partitions[0] == binary_partitions[1] == binary_partitions[2]

def binary_array_partition(array):
    print(f"Input array: {array}")
    number_of_onens = len([digit for digit in array if digit == 1])
    if number_of_onens % 3 != 0:
        return [-1,-1]
    once_counter = 0
    partitions = []
    for index in range(0, len(array)):
       if array[index] == 1:
           once_counter += 1
           if once_counter == number_of_onens / 3 :
               once_counter = 0
               if partitions == []:
                   partitions.append(index)
               else:
                    partitions.append(index + 1)
                    if binary_equality(partitions[0], partitions[1], array):
                        return partitions
                    else:
                        break
    return [-1,-1]           
        
def main():
    print("Question 10")
    print(binary_array_partition([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
    print('\n')
    print(binary_array_partition([1,0,1,0,1]))
    print('\n')
    print(binary_array_partition([1,1,0,1,1]))

    
if __name__ == "__main__":
    main()  