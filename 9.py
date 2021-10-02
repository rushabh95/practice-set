#Write a Python program to append a list to the second list.

x = [1,2,4,5,6]
y = [7,8,9,10,11,12]
i=0
while i < 6:
    x.append(y[i])
    i+=1
print(x)