'''Find the largest sub-array that can be formed by picking consecutive integers.
For example:

Input : [2, 5, 7, 0, 1, 3, 4, 8, 9, 10] Output: [2, 5, 0, 1, 3, 4]'''
l=[2, 5, 7, 0, 1, 3, 4, 8, 9, 10,11,12,13,14,15,16]
l2,l3=[],[]
#Approach o(n^2) 
'''for x in l:
     for y in range(x,-1,-1):
          if (y in l):
             l2.append(l.index(y))
          else:
               break;
     if(len(l2)>len(l3)):
          l3[:]=l2[:]
     l2.clear()
for x in l3:
     print(l[x],end=' ')'''


#Approach2  0(nlogn)
'''
l.sort()
print(l)
for x in range(len(l)-1):
     if l[x]+1 == l[x+1]:
          l2.append(l[x])
          print(l2)
     else:
          if(len(l2)>len(l3)):
               l3[:]=l2[:]
               l2.clear()
if (len(l2)>len(l3)):
     l3[:]=l2[:]
     l2.clear()
print(l2)
print(l3)

#Approach 3 o(n)

for x in l:
     if x-1 not in l:
          temp=x
          while(temp in l):
               l2.append(temp)
               temp+=1
     if(len(l2)>len(l3)):
          l3[:]=l2[:]
     l2.clear()
print(l3)

'''
