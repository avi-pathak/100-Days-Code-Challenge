m,n=[int(x )for x in input("enter the size of Matrix(m*n)----: ").split('*')]
l1=[[0 for x in range(m)] for y in range(n)]           #intialize with 0 according   to the size of matrixe
l2=[[0 for x in range(m)] for y in range(n)]
print("enter the element in row wise")
for x in range(m):
     for y in range(0,n):
          l1[x][y]=int(input())     #taking the input row wise one by one
for i in range(len(l1)):
     for j in range(len(l1[i])):
          l2[i][j]=l1[j][i]                 #make the row of matrix as column and strore the other matrix l2           
for i in range(len(l1)):           
     for j in range(len(l1[i])):
          print(l2[i][j],end=' ')
     print()
