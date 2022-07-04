# 3 Implement quick sorting. For the fulcrum, select:
# (a) A random element in an array
# (b) The last element of the array
# (c) The first element of the array
# (d) The median
# Describe the time complexity of this algorithm with reference to your code

import random
import statistics


def partition(array, low, high):
    # (a) A random element in an array
    pivot = random.randint(low, high)

    # (b) The last element of the array
    # pivot = low

    # (c) The first element of the array
    # pivot = high

    # (d) The median
    # pivot = int(statistics.median([low, (low + high) // 2, high]))

    # running
    array[low], array[pivot] = array[pivot], array[low]
    pivot = low
    i = low + 1

    for j in range(low + 1, high + 1):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i - 1], array[pivot] = array[pivot], array[i - 1]

    return i - 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


input_array = [110, 77, 8, 96, 1, 51, 3]
arr_size = len(input_array)
quick_sort(input_array, 0, arr_size - 1)
print("Sorted array is: ")
for i in range(arr_size):
    print(input_array[i], end=" ")


