'''First Method Is just Sort the element in the heap and atumatically it will be converted
in to min HEAP'''
l=[200,100,50,90,80,40,30,60,20,10]
l.sort()
print(l)

#Second Method just Heapyfy in the rverse order
#complexity is o(n)
def heapyfy(l):
     l2=[0 for x in range(len(l)+1)]
     for i in range(1,len(l)):
          if i==1:
               l2[i]=l[i]
          else:
               l2[i]=l[i]
               par=i//2
               child=i
               while par>=1:
                    if l2[child] > l2[par]:
                         break
                    else:
                         l2[par],l2[child]=l2[child],l2[par]
                    child=par
                    par//=2
     l[:]=l2[1:]
l=[None,200,100,50,90,80,40,30,60,20,10]
heapyfy(l)
print(l)
