from array import *

paw = array('i', [1, 2, 3, 4, 0, 12, 0, 23, 45, 0, 12, 0, 45])
titans = array('i', [])
titan = array('i', [])
for x in paw:
    if x != 0:
        titans.append(x)

    elif x == 0:
        titan.append(x)
titans.extend(titan)
print(titans)

# taking user input according to above program
from array import *

paw = array('i', [])
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    paw.append(x)
print(paw)
titans = array('i', [])
titan = array('i', [])
for x in paw:
    if x != 0:
        titans.append(x)

    elif x == 0:
        titan.append(x)
titans.extend(titan)
print(titans)