def takeInput(section):
     m=int(input("enter the number of student: "))
     l=[[''] for x in range(m)]
     for x in range(m):
          n=0
          print(l)
          while(n<=2):
               k=input("enter {} student {}".format(x+1,section[n]))
               l[x].append(k)
               n+=1
     return l
import csv
with open('Student.csv','w') as newFile:
     section=['Student_Name','Roll NO','Marks']
     csv_writter=csv.writer(newFile,delimiter='\t')
     csv_writter.writerow(['Student_Name','Roll NO','Marks'])
     l=takeInput(section)
     for x in range(len(l)):
          csv_writter.writerow(l[x])
