l=[int(x) for x in input("enter Numbers Seperated By space").split()]
l2=[]
for x in range(len(l)):
     if l[x]!=0:
          l2.append(l[x])
for x in range(l.count(0)):
     l2.append(0)
else:
     print("Result=",l2[:])
