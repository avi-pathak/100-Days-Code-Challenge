l=[0,1,2,3,4,5,6]
min=l[len(l)-1]
for i in range(0,len(l)-1):
     if(l[0]>0):
          min=0
          break
     else:
          if(l[i]+1 != l[i+1]):
               if min>l[i]+1:
                    min=l[i]+1
if min==l[len(l)-1]:
     print(min+1)
else:
     print(min)
