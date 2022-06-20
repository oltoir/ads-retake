# There is a list of integers 1 through 12 ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).
# How many iterations (checks) of binary search is needed to find number * from this array?
# * here the number will be equal to, the length of your name.

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
name = 'Adam'
length_of_name = len(name)


def binary_search(arr, number):
    cnt = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        cnt += 1
        mid = (low + high) // 2
        if arr[mid] == number:
            print(number, "at", mid, "\nNumber of checks:", cnt)
            return mid
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    print(number, "wasn't found\nNumber of checks:", cnt)
    return -1


binary_search(given_list, length_of_name)
print("Length of name", name, length_of_name)
