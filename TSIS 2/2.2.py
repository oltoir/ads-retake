# 2 Create a list of 500 integers using a random number generator.
# Use the sorting algorithms for sorting by choice

import random


def sort_by_choice(array, size):
    for step in range(size):
        min_index = step

        for i in range(step + 1, size):
            if array[i] < array[min_index]:
                min_index = i

        array[step], array[min_index] = array[min_index], array[step]


def random_list_creator(array, size):
    for i in range(size):
        number = random.randint(0, 1000)
        array.append(number)


input_array = []
arr_size = 500
random_list_creator(input_array, arr_size)

sort_by_choice(input_array, arr_size)
print("Sorted array is: ")
for i in range(len(input_array)):
    print(input_array[i], end=" ")