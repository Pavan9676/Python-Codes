# 20) string array total methods
arr1 = ["hi", "welcome", "to", "python"]
arr = ["pavan", "shankar"]
def append1():
    arr1.append("pavan")
    print(arr1)
def clear1():
    arr1.clear()
    print(arr1)
def copy1():
    x = arr1.copy()
    print(x)
def count1():
    x = arr1.count("pavan")
    print(x)
def extend1():
    arr1.extend(arr)
    print(arr1)
def index():
    print(arr1[3])
def pop1():
    print(arr1.pop(4))
def remove1():
    arr1.remove("hi")
    print(arr1)
def reverse1():
    arr1.reverse()
    print(arr1)
def sort1():
    arr1.sort()
    print(arr1)

append1()
copy1()
count1()
extend1()
index()
pop1()
remove1()
reverse1()
sort1()
clear1()