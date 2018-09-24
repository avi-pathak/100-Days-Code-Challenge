n=10
for i in range(0,n):
     j=0
     while j < (n-i):
          print(" ",end='')
          j+=1
     no = 1
     for k in range(0,i+1):
          print("",no,end='')
          no=int((no*(i-k))/(k+1))
     print()
