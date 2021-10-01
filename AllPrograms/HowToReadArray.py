from array import *

arr = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)