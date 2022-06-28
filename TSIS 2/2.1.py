# 1 Change the bubble sort to 'bubble' in both directions.
# The first pass moves the 'top' of the list, the second moves the 'bottom'.
# It continues to work until the need for passes is exhausted.

def bubble_in_both_sort(array, size):
    swapped = True
    top = 0
    bottom = size - 1

    while swapped:
        swapped = False

        for i in range(top, bottom):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
          break

        swapped = False

        bottom = bottom - 1

        for i in range(bottom - 1, top - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        top = top + 1


input_array = [128, 12, 24, 64, 3, 9, 0, 12]
arr_size = len(input_array)
bubble_in_both_sort(input_array, arr_size)

print("Sorted array is: ")
for i in range(len(input_array)):
    print(input_array[i], end=" ")
