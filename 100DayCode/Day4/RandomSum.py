from random import randint as r
while True:
     '''r works works as randint soit generate a random Number Between 0 to 100'''
     a=r(0,100)
     b=r(0,100)
     print("enter the sum")
     print(a," + ",b,"= ")
     print("Correct" if int(input())== a+b else "Try Again")#this function prints correct if the given input is equal to real sum of two above number
