pro,max=1,[0,0,0]
l=[int(x) for x in input().strip().split()]
for x in range(len(l)-1):
     pro=l[x]*l[x+1]
     if(max[2]<pro):
          max[:]=l[x],l[x+1],pro
print(max)
