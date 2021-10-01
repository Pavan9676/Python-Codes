# prime number between range
def Prime():
    for num in range(100, 200):
        if all(num % i != 0 for i in range(2, num)):
            print(num)
Prime()

# fibonacci series using recursion
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1) + f(n-2)
n = int(input("Enter maximum range: "))
for i in range(0, n):
    print(f(i))

# prime number
n = int(input("Enter n value: "))
if n > 2:
    for i in range(2, n):
        if n % i == 0:
            print("is not a prime number")
            break
        else:
            print("prime number")
            break
else:
    print("not a prime number")