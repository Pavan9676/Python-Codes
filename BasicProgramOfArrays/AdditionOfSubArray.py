from array import *
arr = array('i', [])
arr1 = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)
a = int(input("Enter starting value: "))
b = int(input("Enter ending value: "))
for i in range(a-1, b):
    y = arr[i]
    arr1.append(y)
print(arr1)
sum = 0
for i in arr1:
    sum +=i
print(sum)