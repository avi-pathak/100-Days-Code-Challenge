l=['91-896463685','91-66645645','+1-556566','+52-563324563']
num,di='',{}
for x in l:
     for i in x:
          if i=='-':
               break
          num+=i
     if num in di.keys():
          di[num]+=" "+x[3:]
     else:
          di[num]=x[3:]
     num=''
print(di)
li=list(di.values())
for k,v in di.items():
     print(k,"----->",v)
list,m=[],''
for k,v in di.items():
     for i in v.split():
          m+=k+i+","
     list.append(m)
     m=''
     print(li)
for i in list:
     print("NUMB ",l)
