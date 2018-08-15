from itertools import permutations

#First Approach

str,n=[x for x in input().split()]
s=sorted(str)
ans=list(permutations(s,int(n)))
for i in ans:
    for j in i:
        print(j,end='')
    print()
   
#second Approach

s,n = list(map(str,input().split(' ')))
s = sorted(s)
for p in list(permutations(s,int(n))):
    print(''.join(p))
