from array import *
arr = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next element: "))
    arr.append(x)

print("1 = smallest value \n2 = second smallest value\n3 = third smallest value\n4 = fourth smallest value\n"
      "5 = fifth smallest value")
n1 = int(input("Enter your choice: "))
for j in range(n1):
    """if n1==1:                    this is normal logic
        print(arr[0])
        break
    elif n1==2:
        print(arr[1])
        break
    elif n1==3:
        print(arr[2])
        break
    elif n1==4:
        print(arr[3])
        break
    elif n1==5:
        print(arr[4])
        break
    :"""
    print(arr[n1-1])
    break


# 18) print the range of heights which you want
arr = array('i', [])
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter next element: "))
    arr.append(x)
print(arr)
num = sorted(arr)
print("The sorted array: ", num)
y = int(input("enter the nth height of array: "))
print(num[y-1])