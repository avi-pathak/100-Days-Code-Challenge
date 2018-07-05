l=['+91-896463685','+91-66645645','+12-556566','+12-996654533','+52-563324563','+82-665533265']
l2=set([x[:3] for x in l])#this make the set of only country code
li=[[''] for x in range(len(l2))]#this line intialize none the nested list with the number of country
'''So if there are 3 country  in the list it initialize like [ [''] [''] [''] ]'''
i,k=0,1
for y in l2:                  #it pick one by one code from country list
     for x in l:              #it picks one by one number fromthe number list
          if x[:3]==y:        #it campare whether the first 3 letter are match frma any on in the number list
               li[i][0]+=x+","#if matched add to the result like [['+915568766'][][]]
     i+=1
     '''printing the result'''
for x in range(len(li)):
     for y in range(len(li[x])):
          print("NUMB",k,li[x][y])
          k+=1
     print()
