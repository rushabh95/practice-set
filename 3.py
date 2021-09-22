#Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

a = int(input("enter a number: "))
b = int(input("enter other number: "))

c = a+b
if (c<20 and c>15):
    print("20")
else:
    print(c)