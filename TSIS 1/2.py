# Suppose the size of the list is doubled.
# How would the maximum number of checks change? n + 1

input_arr = []


def read(arr, lines_to_read):
    with open('data.txt', 'r') as f:
        for i in range(0, lines_to_read.stop):
            if i in lines_to_read:
                arr.append(f.readline()[:-1][3:])
            else:
                f.readline()


# function for binary search to find a name in sorted array
def binary_search(arr, name):
    cnt = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        cnt += 1
        mid = (low + high) // 2
        if arr[mid] == name:
            print(name, "at", mid, "\nNumber of checks:", cnt)
            return mid
        elif arr[mid] < name:
            low = mid + 1
        else:
            high = mid - 1
    print(name, "wasn't found\nNumber of checks:", cnt)
    return -1


name_to_find = 'Adam'

# first 32 elements
read(input_arr, range(0, 32))
binary_search(input_arr, name_to_find)

# another 32 elements
read(input_arr, range(32, 64))
binary_search(input_arr, name_to_find)
