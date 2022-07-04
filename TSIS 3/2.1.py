# 1 Write a recursive function to count the items in a list
def count_list(array):
    if not array:
        return 0
    return 1 + count_list(array[1:])


input_array = [1, 3, 5, 15, 25, 46]
print(count_list(input_array))
