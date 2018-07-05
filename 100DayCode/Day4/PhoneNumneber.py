l=['+91-896463685','+91-66645645','+12-556566','+12-996654533','+52-563324563','+82-665533265']
l2=['+91','+12','+52','+82']
li=[[''] for x in range(len(l2))]
i,k=0,1
for y in l2:
     for x in l:
          if x[:3]==y:
               li[i][0]+=x+","
     i+=1
for x in range(len(li)):
     for y in range(len(li[x])):
          print("NUMB",k,li[x][y])
          k+=1
     print()
