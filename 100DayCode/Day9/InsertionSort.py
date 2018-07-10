l=[int(x) for x in input("enter the Number with Spaces").strip().split()]
flag=False
for i in range(1,len(l)):
     key=l[i]
     j=i-1
     while(j>=0 and key<l[j]):
          l[j+1]=l[j] #shifting till we find the right position for key
          j-=1
     l[j+1]=key  #storing the key at its correct positiion
print(l)
