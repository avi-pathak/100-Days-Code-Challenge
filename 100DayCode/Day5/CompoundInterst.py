from math import pow
p=int(input("Enter the Amount"))#taking the pricipal amount
r=float(input("Enter the rate"))#taking the rate of interest
t=int(input("Enter the year"))  #taking the time in for of year
a=p*(pow((1+r/100),t)-1)        #applying the formula
print("compound iNTEREST iS",a) #printing the result   
