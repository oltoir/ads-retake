# 2 Find the largest number in the list with the recursive function
import sys


def maxi_maxi(array, maxi):
    if not array:
        return maxi
    maxi = max(array[0], maxi)
    return maxi_maxi(array[1:], maxi)


input_array = [125, 2, 5, 10, 25]
print(maxi_maxi(input_array, -sys.maxsize))
