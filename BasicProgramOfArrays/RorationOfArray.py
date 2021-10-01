# cyclically rotate an array by one
from array import *
arr = array('i', [])
arr1 = array('i', [])
arr2 = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
for i in arr:
    if i != arr[len(arr)-1]:
        arr1.append(i)
    else:
        arr2.append(i)
print(arr)
print(arr1)
print(arr2)
arr2.extend(arr1)
print(arr2)