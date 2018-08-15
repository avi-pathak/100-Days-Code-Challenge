import itertools
s,n = list(map(str,input().split(' ')))
s = sorted(s)
for i in range(1,int(n)+1):
    for j in list(itertools.combinations(s,i)):
                  print("".join(j))
