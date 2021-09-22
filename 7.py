#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math


def difference(a,b,c,d):
    t = b-a
    s = d-c
    l = ((t*t)+(s*s))
    return(math.sqrt(l))

x1 = int(input("enter x1 coordinate: "))
x2 = int(input("enter x2 coordinate: "))
y1 = int(input("enter y1 coordinate: "))
y2 = int(input("enter y2 coordinate: "))

if x1<x2:
    a=x1
    x1=x2
    x2=a
if y1<y2:
    b=y1
    y1=y2
    y2=b
r = difference(x1,x2,y1,y2)
print("the difference between the coordinated is ",r)
