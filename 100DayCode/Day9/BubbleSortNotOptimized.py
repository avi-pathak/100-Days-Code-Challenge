l=[int(x) for x in input("enter the Number with Spaces").strip().split()]
k=len(l)
for i in range(len(l)):
     for j in range(len(l)-i-1):
          if l[j] > l[j+1]:
               l[j],l[j+1]=l[j+1],l[j] #swapping the next elemnt is less than it left element

               '''this Method is Not optimized Bcoz Nomatter Array is already
               sorted Or Not it will run N*2'''
print(l)
