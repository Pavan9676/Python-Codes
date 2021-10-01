year = int(input("Enter a year for check leaf year or not: "))
if (year % 4 ==0 and year % 100 != 0 or year % 400 ==0):
    print("given year is leaf year")
else:
    print("given year is not a leaf year")