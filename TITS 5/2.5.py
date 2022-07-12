def sortList(array):
    length = len(array)

    for item in range(length):
        minimum = item

        for i in range(item + 1, length):
            if array[i] < array[minimum]:
                minimum = i
        (array[item], array[minimum]) = (array[minimum], array[item])
    return array


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(l,r,arr):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi - 1, nums)
        quicksort(pi + 1, r, nums)
    return nums


a = [3,4,5,1,2,6,7,100,99,98,97,96,95,80,79]
b = [3,4,5,1,2,6,7,101,94,93,92,91,90,82,81]
c = [3,4,5,1,2,6,7,102,89,88,87,86,85,84,83]

d = a + b
d = list(set(d)- set(c))
print(sortList(d))
bubbleSort(d)
print(d)
mergeSort(0,len(d)-1,d)
print(d)
insertionSort(d)
print(d)
quicksort(0,len(d)-1,d)
print(d)

