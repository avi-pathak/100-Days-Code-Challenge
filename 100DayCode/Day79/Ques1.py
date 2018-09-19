n = int(input("Enter the size matrix MUST BE ODD"))

num = [i for i in range(1,n*n + 1)]

mat = [[0 for i in range(n)] for j in range(n)]

magic_number = int(n*(n**2+1) / 2)
print(magic_number," is the mnagic number")

num_i = 1
i = int(n/2)
j = n-1
mat[i][j] = "1"
while num_i < len(num):
     i-=1
     j+=1
     if i == -1 and j == n:
          i = 0
          j = n-2
     if i == -1:
          i=n-1
     if j == n:
          j=0
     if mat[i][j] != 0:
          i+=1
          j-=2
     mat[i][j] = str(num[num_i])
     num_i+=1
print()

print("Magic Matrix is :")

print()
for i in mat:
     print(" ".join(i))

