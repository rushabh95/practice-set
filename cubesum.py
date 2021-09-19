#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers
#smaller than the specified number.

def cubesum(a):
    sum=0
    t = a-1
    while t>0:
        sum = sum + (t*t*t)
        t-=1
    return(sum)
b = int(input("enter a number: "))
print(cubesum(b))
