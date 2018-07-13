n=int(input("enter the Number  "))
l,flag=[],1
if n<0:
        n*=-1
        flag=0
while(n>0):
        l.append(n%2)
        n=int(n/2)
if flag==0:
        l.append(1)
else:
        l.append(0)

print(l[::-1])
