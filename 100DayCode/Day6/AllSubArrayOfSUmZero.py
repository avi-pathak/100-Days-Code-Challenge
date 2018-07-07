l=[int(x) for x in input("enter Numbers Seperated By space").split()]
sum=0
for i in range(len(l)):
     for j in range(i,len(l)):  #creating loop for all posiible subarray from elemnt liyh index
          sum+=l[j]             #calculating the sum
          if(sum==0):           
               print(l[i:j+1])  #if sum equal zero the printing the particular sub array
     sum=0
