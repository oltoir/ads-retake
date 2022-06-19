# You have a sorted list of
# 64 names and you are looking
# for a value in it using the
# binary search method.
# What is the maximum number of checks it can take? 6

arr = []
with open('data.txt', 'r') as f:
    for i in range (64):
        arr.append(f.readline()[:-1][3:])

# function for binary search to find a name in sorted array
def binary_search(arr, name):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == name:
            return mid
        elif arr[mid] < name:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(arr, 'Zack'))