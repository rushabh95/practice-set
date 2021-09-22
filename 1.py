# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
#tuple with those numbers.
#Sample data : 3, 5, 7, 23
m=()
n = []
i = 0
while i < 4:
    a = int(input("enter a number: "))
    n.append(a)
    i+=1
print(n)
m = tuple(n)
print(m)
