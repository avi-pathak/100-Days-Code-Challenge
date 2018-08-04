degree=int(input("Enter the Dgree of equation:- "))
print("---------------------------------------------------")
n1=input("enter the equation of\n for example of degree 2\n(1*x^2+1*x+integer):- ")
print("----------------------------------------------------------------------------")
while(True):
     n=n1[:]
     ValueOfX=int(input("Enter the value of x on which You want to calculate:- "))
     print("----------------------------------------------------------------------")
     n=n.replace("x",str(ValueOfX))
     n=n.replace("^",'**')
     print("Value Of the Equation")
     print(eval(n))
     repeat=input("Enter Y to calculate on another X Or N to exit:- ")
     if repeat == 'Y' or repeat == 'y':
          continue
     elif repeat == 'N' or repeat == 'n':
          break
     else:
          print("Invalid Input We are Quiting The Softeware")
          print("--------------------------------------------------------------")
          print()
print("Thanks For using Our Application")
