# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 /2014

t = (11, 12, 2014)
print("The examination will start from : ")
i=0
while i < 3:
    print(t[i], end ="")
    i+=1
    if i < 3:
        print("/", end="")

