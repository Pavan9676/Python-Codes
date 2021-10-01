from array import *
arr = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
def peak():
    m = arr[0]
    for i in range(len(arr)):
        if m < arr[i]:
            m = arr[i]
    print(m)
peak()

# another method
arr = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
def peak1():
    m = arr[0]
    for i in arr:
        if m < i:
            m = i
    print("The peak value of the given array is: ", m)
peak1()
# Direct method for array
def Direct():
    arr = array('i', [])
    n = int(input("Enter size of array: "))
    for i in range(n):
        x = int(input("Enter the next value: "))
        arr.append(x)
    print(arr)
    print("max value of tha given array: ", max(arr))
    print("max value of tha given array: ", min(arr))
Direct()