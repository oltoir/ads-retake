# 3 Implement the merge sort function without the slice operator.

def merge_without_slice_sort(array, size):
    if size > 1:
        r = size // 2
        l = []
        m = []

        for i in range(r):
            l.append(array[i])
        for i in range(r, size):
            m.append(array[i])

        l_size = len(l)
        m_size = len(m)

        merge_without_slice_sort(l, l_size)
        merge_without_slice_sort(m, m_size)

        i = j = k = 0

        while i < l_size and j < m_size:
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1

        while i < l_size:
            array[k] = l[i]
            i += 1
            k += 1

        while j < m_size:
            array[k] = m[j]
            j += 1
            k += 1


input_array = [128, 12, 24, 64, 3, 9, 0, 12]
arr_size = len(input_array)
merge_without_slice_sort(input_array, arr_size)

print("Sorted array is: ")
for i in range(arr_size):
    print(input_array[i], end=" ")
