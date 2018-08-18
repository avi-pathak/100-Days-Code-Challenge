''' i just use simple hashing to count the accourence of each word using Dictionaries'''

from collections import OrderedDict
n=int(input())
d=OrderedDict()
for _ in range(n):
    string=input()
    if string not in d.keys():
        d[string]=1
    else:
        d[string]+=1
    
print(len(d))
for k in d.values():
    print(k, end=' ')
