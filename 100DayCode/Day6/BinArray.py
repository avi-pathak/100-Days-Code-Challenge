from time import clock as c #it only for calculating the excution time
binarr=[int(x) for x in input("enter Numbers Seperated By space").split()] #taking Input
t1=c()
l2=[0 for x in range(binarr.count(0))] #at start of result push all no of Zero present the above list
for x in range(binarr.count(1)):     #appending all no of One present in the above list
    l2.append(1)
t2=c()
print(l2,t2-t1) #printing result and the excution time
