l=[int(x) for x in input("Enter the Numbers Sepeeated By Space= ").strip().split()]
s=set()
for x in range(len(l)):
    if l[x] in l[x+1:]:
         s.add(l[x])
         break
print(s)
