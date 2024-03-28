


class BinaryExecuter:
    def __init__(self,array):
        self.array = array

    def get_array(self):
        return self.array

    def set_array(self, new_array):
        self.array = new_array

    def binary_trim_prefix(self,array,index = 0):    
        if array[index] == 1:
            return array
        else:
            return self.binary_trim_prefix(array[index+1:])

    def partition_devider(self,partition_i, partition_j):
        partition_a = self.array[0:partition_i + 1]
        partition_b = self.array[partition_i + 1:partition_j]
        partition_c = self.array[partition_j:len(self.array)]
        # print(f'Partition dediver  \n  0 : i ->  {partition_a}\n  i+1 : j-1 -> {partition_b}\n  j : -1 -> {partition_c}')
        return [
            self.binary_trim_prefix(partition_a, 0),
            self.binary_trim_prefix(partition_b, 0),
            self.binary_trim_prefix(partition_c, 0),
        ]

    def binary_equality(self,partition_i, partition_j):
        # print(f"partition_i: {partition_i}, partition_j: {partition_j}, self.array: {self.array}")
        binary_partitions = self.partition_devider(partition_i, partition_j)
        # print(f"binary_partitions: {binary_partitions}")
        return binary_partitions[0] == binary_partitions[1] == binary_partitions[2]

    def binary_array_partition(self,):
        print(f"Input array: {self.array}")
        number_of_onens = len([digit for digit in self.array if digit == 1])
        if number_of_onens == 0:
            return [0, len(self.array) - 1]
        if number_of_onens % 3 != 0:
            return [-1,-1]
        once_counter = 0
        partitions = []
        for index in range(0, len(self.array)):
            if self.array[index] == 1:
                once_counter += 1
                if once_counter == number_of_onens / 3 :
                    once_counter = 0
                    if partitions == []:
                        partitions.append(index)
                    else:
                            partitions.append(index + 1)
                            if self.binary_equality(partitions[0], partitions[1]):
                                return partitions
                            else:
                                break
        return [-1,-1]           
        
def main():
    print("Question 10")
    binary_executer = BinaryExecuter([])
    binary_executer.set_array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    partitions = binary_executer.binary_array_partition()   
    print(f"Partitions: {partitions}")
    
    
    # print(binary_array_partition([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
    # print('\n')
    # print(binary_array_partition([1,0,1,0,1]))
    # print('\n')
    # print(binary_array_partition([1,1,0,1,1]))

    
if __name__ == "__main__":
    main()          