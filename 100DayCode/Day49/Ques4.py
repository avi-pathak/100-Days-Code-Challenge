''this is the problem of appliction of sorting''

m,n=list(map(int,input().split()))
l=[]
for _ in range(m):
    l1=list(map(int,input().split()))
    l.append(l1)
k=int(input())

size=lambda l: l[k]
l.sort(key=size)
for i in l:
    for j in i:
        print(j,end=' ')
    print()
