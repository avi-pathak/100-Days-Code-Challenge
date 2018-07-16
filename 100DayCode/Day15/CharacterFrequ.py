s=input("enter string")
d={}
for x in s:
        if x not in d:
                d[x]=1
        else:
                d[x]+=1
print(d)

# 2nd Apoproach

s=input("enter string")
for x in s:
        print("%s : %d"%(x,s.count(x)))
