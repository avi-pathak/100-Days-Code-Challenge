n,m=[int(x) for x in input().split()]
l=int((m-3)/2)
k=1
for x in range(int(n/2)):
     for y in range(l):
          print("-",end='')
     for y in range(k):
          print(".|.",end='')
     for y in range(l):
          print("-",end='')
     l-=3
     k+=2
     print()
print("-"*int((m-7)/2),end='')
print("WELCOME",end='')
print("-"*int((m-7)/2))
l=int((m-6)/3)
k=3
for x in range(int(n/2)):
     for y in range(k):
          print("-",end='')
     for y in range(l):
          print(".|.",end='')
     for y in range(k):
          print("-",end='')
     l-=2
     k+=3
     print()
     
