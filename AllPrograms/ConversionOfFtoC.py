def paw():
    print("choose options 1 or 2 only")
    print("if 1 is click the conversion of  celsius to fahrenheit")
    print("if 2 is click the conversion of  fahrenheit to celsius")
    a = int(input("Enter which one you want: "))
    if a == 1:
        b = int(input(" Give the celsius value: "))
        f = (b*1.8)+32
        print(b, "value of fahrenheit value is: ", f)
    elif a == 2:
        b = int(input("Give the fahrenheit value: "))
        c = (b-32)/1.8
        print(b, "value of celsius value is: ", c)
    else:
        print("choose 1 or 2 only")
paw()