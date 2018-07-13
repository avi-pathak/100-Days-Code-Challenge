from random import randint
list=[0,1,2,
      3,4,5,
      6,7,8]
def show():
     print(list[0],'|',list[1],'|',list[2],'|')
     print(list[3],'|',list[4],'|',list[5],'|')
     print(list[6],'|',list[7],'|',list[8],'|')
def isempty(n):
     if(list[n]!='X' and list[n]!='O'):
          return True
     else:
          return False
def allEmpty():
     return (all(x=='X' or x=='O' for x in list))
def whoWins(char):
     if list[0]==char and list[1]==char and list[2]==char:
          return True
     elif list[3]==char and list[4]==char and list[5]==char:
          return True
     elif list[6]==char and list[7]==char and list[8]==char:
          return True
     elif list[0]==char and list[3]==char and list[6]==char:
          return True
     elif list[1]==char and list[4]==char and list[4]==char:
          return True
     elif list[2]==char and list[5]==char and list[8]==char:
          return True
     elif list[0]==char and list[4]==char and list[8]==char:
          return True
     elif list[2]==char and list[4]==char and list[6]==char:
          return True
show()
while True:
     if allEmpty():
          print("Match Draw")
          break
     if whoWins('X'):
          print('YOU WIN')
          break;
     if whoWins('O'):
          print('Computer Wins')
          break;
     key=int(input("enter the postion wheree you want to start:  "))
     if isempty(key):
          list[key]='X'
     else:
          print("the postion is already taken tru anather One ")
     while True:
          comp=randint(0,8)
          if isempty(comp):
               list[comp]='O'
               show()
               break
