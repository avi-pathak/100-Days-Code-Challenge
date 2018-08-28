def valley(l):
     if len(l)<=2:
          return False
     else:
          l1=l[:]
          deq_seq=[]
          i=0
          while(l[i]>l[i+1] and i<len(l)):
               deq_seq.append(l[i])
               l1.remove(l[i])
               i+=1
          if len(l1) == 1:
               return True
          i=0
          return all(l1[i]<l1[i+1] for i in range(len(l1)-1))
