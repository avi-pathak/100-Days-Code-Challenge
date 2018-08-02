UserInput=[int(x) for x in input("Enter numbers seprated By Spaces").strip().split()] #Taking Input
Result=[-1 for x in range(len(UserInput)+1)]#Creating Result Array
temp=[0 for x in range(max(UserInput)+1)]#Creating The temp. array

for i in range(len(UserInput)):
     temp[UserInput[i]]+=1#   Countingt Frequency

for i in range(1,len(temp)):
     temp[i]+=temp[i-1]# Summing the temp Array

for i in range(1,len(Result)-1):
     Result[temp[UserInput[i]]] = UserInput[i]# Assing the Correct element at the correct location
     temp[UserInput[i]]-=1

for i in Result:
     if i >= 0:
          print(i)#Printing the result
