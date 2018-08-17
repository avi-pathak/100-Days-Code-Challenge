'''
in this Problem we need to just make a dict with their values and sum the value if any existing key comes again
'''
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for _ in range(n):
    list1=list(input().split())
    if len(list1) == 3:
        name=list1[0] + " " + list1[1]
    else:
        name=list1[0]
    k=d.get(name,0)
    if k==0:
        d[name]=0
    price=list1.pop()
    d[name]+=int(price)
    
for k,v in d.items():
    sum=k + " " +str(v)
    print("".join(sum))
