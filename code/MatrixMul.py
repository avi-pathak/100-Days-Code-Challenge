"""IT ISD THE PROGRAM WHICH TAKE TWO MATRIX AS INPUT AND CALCULATE MULTICATION AND PRINT THE RESULT AS 3RD MATRIX"""
m,n=[int(x )for x in input("enter the size of Array").split()]
k,l=[int(x )for x in input("enter the size of Seconf Array").split()]
result=[[0 for x in range(k)]for y in range(l)]
l1=[[0 for x in range(m)] for y in range(n)]
l2=[[0 for x in range(k)] for y in range(l)]
for x in range(n):
     l1.append([])
for x in range(n):
     l2.append([])
if m!=l:
     print("Multipication Note Possible try Anather Size of matrix")
else:
     print("enter the element in row wise")
     for x in range(m):
          for y in range(0,n):
               l1[x][y]=int(input())
     print("enter the element in row wise")
     for x in range(m):
          for y in range(0,n):
               l2[x][y]=int(input())
     for x in range(m):
          for y in range(n):
               for k in range(l):
                    result[x][y]+=l1[x][k]*l2[k][y]
     print("\t\tMatrix Multipication is")
     for i in range(len(result)):
          for j in range(len(result[i])):
               print(result[i][j],end=' ')
          print()
