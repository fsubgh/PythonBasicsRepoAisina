#Task 1
#m: int = int(input())
#n: int = int(input())
#for i in range(1, m+1):
 #   if i % 17 == 0 or i % 10 == 9 or (i % 3 and i % 5 == 0):
  #      print(i)

#Task 2
#n: int = int(input())
#for i in range(1, n + 1):
 #   if n in range(5, 9):
  #      continue
   # if n in range(17, 37):
    #    continue
    #if n in range(78, 87):
     #   continue
      #  print(n)


#Task 3
n: int = int(input())
if n <= 9:
    print(n)
for i in range(n):
    for j in range(3):
        print(i, end=" ")
        print()
