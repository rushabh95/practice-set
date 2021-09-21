#Write a Python program to test whether a number is within 100 of 1000 or 2000.
a = int(input("enter a number: "))
if a<=99:
    print("number is less than 100")
elif (a>=100 and a<=999):
    print("number is between 100 and 1000")
elif (a>=1000 and a<=1999):
    print("number is between 1000 and 2000")
else:
    print("greater than 2000")
