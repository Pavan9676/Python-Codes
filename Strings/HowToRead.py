# read only characters array item must be unicode character
from array import *

arr = array("u", [])
x = int(input("Enter size of string: "))
for i in range(x):
    n = (input("Enter the next string: "))
    arr.append(n)
print(arr)