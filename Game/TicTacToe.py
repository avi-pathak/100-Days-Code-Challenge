from random import randint
list=[0,1,2,
      3,4,5,
      6,7,8]
def show():
     print(list[0],'|',list[1],'|',list[2],'|')
     print(list[3],'|',list[4],'|',list[5],'|')
     print(list[6],'|',list[7],'|',list[8],'|')
def isempty(n):
     if(list[n]!='#' and list[n]!='*'):
          return True
     else:
          return False
def allFull():
     return (all(x=='#' or x=='*' for x in list))
def whoWins(char):
     if list[0]==char and list[1]==char and list[2]==char:
          return True
     elif list[3]==char and list[4]==char and list[5]==char:
          return True
     elif list[6]==char and list[7]==char and list[8]==char:
          return True
     elif list[0]==char and list[3]==char and list[6]==char:
          return True
     elif list[1]==char and list[4]==char and list[7]==char:
          return True
     elif list[2]==char and list[5]==char and list[8]==char:
          return True
     elif list[0]==char and list[4]==char and list[8]==char:
          return True
     elif list[2]==char and list[4]==char and list[6]==char:
          return True
show()
while True:
     if whoWins('*'):
          print('--------------Computer Wins---------------')
          break;
     key=int(input("enter the postion where you want to start:  "))
     if isempty(key):
          list[key]='#'
     else:
          print("the postion is already taken try anather One ")
     while True:
          comp=randint(0,8)
          if whoWins('#'):
               print('---------------YOU WIN------------------')
               break;
          elif allFull():
               print("---------------Match Draw----------------")
               break;
          elif isempty(comp):
               list[comp]='*'
               show()
               break
