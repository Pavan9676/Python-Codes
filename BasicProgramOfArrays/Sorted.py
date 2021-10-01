from array import *
arr = array('i', [])
n = int(input("Enter size of the array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)
num = sorted(arr)
print(num)

# ascending and descending of array
from array import *
arr = array('i', [])
n = int(input("Enter size of the array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)
num = sorted(arr)
print(num)
print(num[::-1])