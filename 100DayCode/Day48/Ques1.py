''' i use beautifull eval function to evaluate the command'''
from collections import deque
n=int(input())
d=deque()
for _ in range(n):
    l=list(input().split())
    cmd=l[0]
    if len(l)>=2:
        value=l[1]
        k="d."+cmd+"("+ str(value) +")"
    else:
        k="d."+cmd+"(" +")"
    eval(k)
for i in list(d):
    print(i,end=' ')
