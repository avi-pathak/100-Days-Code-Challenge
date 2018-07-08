l=[int(x) for x in input("Enter the Numbers Sepeeated By Space= ").strip().split()]

for x in range(len(l))
    if l[x] in l[x+1:]:
         printf("First Duplicate  ",l[x])
         break
