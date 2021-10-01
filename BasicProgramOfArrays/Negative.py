# take user input print negetive elements end of the array
from array import *
arr = array('i', [])
arr1 = array('i', [])
arr2 = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)
for i in range(len(arr)):
    if arr[i] < 0:
        y = arr[i]
        arr1.append(y)
    else:
        a = arr[i]
        arr2.append(a)
print(arr2)
print(arr1)
arr2.extend(arr1)
print(arr2)