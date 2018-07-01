def push(l,item):
     l.append(item)
def pop(l):
     return(l.pop())

l=[]
while True:
     print("enter the option...")
     k=int(input("enter 1 for push and 2 for pop the element 3 for exit"))
     if k==1:
          item=input("enter the element")
          push(l,item)
          print("Item Pushed In To Stack")
     elif k==2:
          if not l:
               print("Stack Is Empty")
          else:
               item=pop(l)
               print(item,"Is Poped From Stack")
     elif k==3:
          break;
     else:
          print("Invalid Choice Plz Try again")
