l=[]
n=int(input())
for x in range(n):
     k=int(input())
     l.append(k)
d={}
mx=0
for i in range(len(l)):
     d[l[i]]=0
     for j in range(i+1,len(l)):
          l1=[]
          if l[j] % l[i] == 0:
               l1.append(l[j])
               temp=l[j]
               for k in range(j+1,len(l)):
                    if l[k] % temp == 0:
                         l1.append(l[k])
                         temp = l[k]
          if mx < len(l1):
               d[l[i]]=len(l1)
               mx=len(l1)
print(max(d.values())+1)
