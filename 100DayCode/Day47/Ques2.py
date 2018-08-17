import collections as c
d=c.defaultdict(list)
m,n=list(map(int,input().split()))
for x in range(m):
    k=input()
    d[k].append(str(x+1))
''''
this code will return for k
a
a
b
a
b
and the default dict of list will be

defaultdict(<class 'list'>, {5: ['1', '2', '3', '4', '5']})

now we just need to print the each keys value from groub b
''''
for y in range(n):
    k=input()
    if k in d.keys():
        print(" ".join(d[k]))
    else:
        print(-1)
