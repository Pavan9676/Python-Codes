from array import *
arr = array('i', [])
arr1 = array('i', [])
arr2 = array('i', [])
n = int(input("Enter range of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
print(arr)
i = 1
for i in range(len(arr)):
    if arr[i-1] + 1 != arr[i]:
        x = arr[i-1] + 1
        arr1.append(x)
arr2 = sorted(arr1)
for i in arr2:
    print(i)
    break