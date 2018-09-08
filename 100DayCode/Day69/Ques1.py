course , grade , stu = [] , [] ,{}
id,grades=[],{}
string=''
names = []
def getinput():
     while True:
          s1 = input()
          if s1 != 'Students':
               
               s=list(s1.split('~'))
               course.append(s)
          else:
               break
     while True:
          s1 = input()
          if s1 != 'Grades':
               r,n = s1.split('~')
               stu[r] = n
               id.append(r)
          else:
               break
     while True:
          s1 = input()
          if s1 != 'EndOfInput':
               c,con,session,stuid,grade=s1.split('~')
               if grade == 'AB':
                    g=9
               elif grade == 'A':
                    g=10
               elif grade ==  'B':
                    g = 8

               elif grade == 'BC':
                    g = 7
               elif grade  == 'C':
                    g = 6
               elif grade  == 'Cd':
                    g = 5
               elif grade  == 'CD':
                    g = 4
               
               if stuid not in grades.keys():
                    grades[stuid] = g     
               else:
                    grades[stuid] = (grades[stuid] + g) / 2
          else:
               break
     

def printOutput():
     id.sort()
     result=''
     for i in range(len(id)):
          result += id[i] + "~" + stu[id[i]]
          if id[i] in  grades.keys():
               avg = grades[id[i]]
               print(result+"~%.1f"%(avg))
          else:
               avg = 0
               print(result+"~%d"%(avg))
          result=''



getinput()
printOutput()
