from time import clock as c
binarr=[int(x) for x in input("enter Numbers Seperated By space").split()]
t1=c()
l2=[0 for x in range(binarr.count(0))]
for x in range(binarr.count(1)):
    l2.append(1)
t2=c()
print(l2,t2-t1)
