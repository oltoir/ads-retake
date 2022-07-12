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


def intersect_two(nums1, nums2):
    m = {}
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    for i in nums1:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    result = []
    for i in nums2:
        if i in m and m[i]:
            m[i] -= 1
            result.append(i)
    return result

def intersect(a,b,c):
    return intersect_two(intersect_two(a,b),c)


a = [3,4,5,1,2,6,7,100,99,98,97,96,95,80.79]
b = [3,4,5,1,2,6,7,101,94,93,92,91,90,82,81]
c = [3,4,5,1,2,6,7,102,89,88,87,86,85,84,83]

print(intersect(sortList(a),sortList(b),sortList(c)))
print(intersect(quicksort(0,len(a)-1,a),quicksort(0,len(b)-1,b),quicksort(0,len(c)-1,c)))
bubbleSort(a)
bubbleSort(b)
bubbleSort(c)
print(intersect(a,b,c))
insertionSort(a)
insertionSort(b)
insertionSort(c)
print(intersect(a,b,c))
mergeSort(0,len(a)-1,a)
mergeSort(0,len(b)-1,b)
mergeSort(0,len(c)-1,c)
print(intersect(a,b,c))

