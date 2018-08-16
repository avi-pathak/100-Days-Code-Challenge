import itertools
s,n = list(map(str,input().split(' ')))
s = sorted(s)
for j in list(itertools.combinations_with_replacement(s,int(n))):
    print("".join(j))
