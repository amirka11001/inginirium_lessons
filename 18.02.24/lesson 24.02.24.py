'''import numpy

arr = numpy.empty([2, 2], dtype= int)
print(arr)

arr2 = numpy.ones([2, 2], dtype= int)
print(arr2)

arr3 = numpy.arange(10)
print(arr3)
print(arr3[slice(2, 7, 2)])
print(arr3[::])'''
import numpy

arr1 = input()
arr2 = input()

inner = True

def est(array1, array2):
    for i, e in enumerate(arr1):
        if (e in arr1) == False:
            return False
    return True

print(est(arr1, arr2))