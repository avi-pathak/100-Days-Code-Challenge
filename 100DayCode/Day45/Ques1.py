from itertools import product
list1=[eval(x) for x in input().strip().split()]
list2=[eval(x) for x in input().strip().split()]
ans=list(product(list1,list2))
for i in ans:
    print(i,end=' ')
