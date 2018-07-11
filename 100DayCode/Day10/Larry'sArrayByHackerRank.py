t = int(input())
for i in range(t):
    a = 0
    n = int(input())
    li = [int(x) for x in input().split()]
    for j in range(n):
        for k in range(j+1,n):
            if li[j]>li[k]:
                a += 1
    if a%2 == 0:
        print("YES")
    else:
        print("NO")
