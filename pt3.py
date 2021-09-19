#Write a Python function to check whether a number is divisible by another number.
# Accept two integers values form  the user.

def divisible (x,y):
    if x%y == 0:
        return(1)
    else:
        return(0)

a = int(input("enter first number: "))
b = int(input("enter second number: "))
f = divisible(a,b)
if f == 1:
    print("1st number is divisible by other")
else:
    print("not divisible")