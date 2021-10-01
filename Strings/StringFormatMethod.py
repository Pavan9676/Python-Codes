print("The string is: %10s"%("ravi"))
print("The string is: %-10s"%("ravi"))
print("The string is: %.4s"%("codetantra"))
print("The string is: %10.4s"%("codetantra"))

# Number string format method
print("The number is: %4d"%(34))
print("The number is: %010d"%(34))
print("The number is: %012.2f"%(34.1234))

# String format methods
print("{} is a great person".format("pavan"))
print("{} is a great {}".format("pavan", "person"))
print("{1} is a great {0}".format('pavan', 'person'))
print("{0:.4s}".format("codetantra"))
print("{0:6.4s}".format("codetantra"))
print("{0:4d}".format(34))
print("{0:10d}".format(34))
print("{0:010.2}".format(3.124))
