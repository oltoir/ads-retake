# Write code for binary search (preferably in Python).
# It should take 1) a list (consisting of numbers) and 2) a certain desired number to search for.
# It should give the correct answer: the number of iterations passed in the binary search.

import random


def binary_search(arr, number):
    if sorted(arr) != arr:
        arr = sorted(arr)
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


random_list = []
for i in range(0, 8):
    number = random.randint(0, 8)
    random_list.append(number)

searching_number = 3
for i in range(0, 64):
    number = random.randint(0, 100)
    random_list.append(number)

searching_number = 21
binary_search(random_list, searching_number)
