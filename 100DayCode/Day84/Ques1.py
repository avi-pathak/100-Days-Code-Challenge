l=[]
n=int(input())
for x in range(n):
     k=int(input())
     l.append(k)
ls=[1 for i in range(len(l))]
for i in range(len(l)):
     for j in range(0,i):
          if l[i] % l[j] == 0 and ls[i] < ls[j]+1:
               ls[i]=ls[j]+1
print(max(ls))
