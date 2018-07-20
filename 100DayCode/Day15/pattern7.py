
'''Pattern-7
-------------:
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
----------------------------
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):#each row
  for j in range(1,n+1):#each column
    print(n+1-j,end=" ")#print the elemen
   print()#it is for going to the new line
