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
    cnt = 0
    high = len(arr) - 1
    while low <= high:
        cnt += 1
        mid = (low + high) // 2
        if arr[mid] == name:
            return mid, cnt
        elif arr[mid] < name:
            low = mid + 1
        else:
            high = mid - 1
    return -1, cnt

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(nums, 5))

# print(binary_search(arr, 'Zack'))