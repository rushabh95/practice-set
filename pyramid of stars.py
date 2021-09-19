# Write a program to print
#     *
#    ***
#   *****
#  *******
# *********
i = 1
while i <= 5:
  j = 5
  while j >= 1:
    if j > i:
      print(" ", end='')
    else:
      print("*", end='')
    j -= 1
  k  = 2
  while k <= 5:
      if k <= i:
          print("*",end='')
      else:
          print(" ",end ='')
      k +=1
  print()
  i += 1
