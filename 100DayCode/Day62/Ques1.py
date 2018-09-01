def multpoly(p1,p2):
     if len(p1) == 0 or len(p2) == 0:
           return []
     i,j=0,0
     p3=[]
     while(i < len(p1)):
          p1[i] = list(p1[i])
          i+=1
     while(i < len(p2)):
          p2[i] = list(p2[i])
          i+=1
     i,j=0,0
     while(i < len(p1)):
          for k in p2:
               c = p1[i][0] * k[0]
               p = p1[i][1] + k[1]
               loc= searchpow(p3,p)
               if loc == None:
                    p3.append([c,p])
               else:
                    loc[0] += c
          i+=1
     result=[tuple(x) for x in p3 if x[0]!=0]
                    
     return result
def searchpow(p3,pow):
     if len(p3) == 0:
          return None
     for i in p3:
          if i[1] == pow:
               return i
     return None
     
     
     
     
     
     '''OUTPUT
      
        multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])  
        
        [(1, 3),(-1, 0)]  '''
        
