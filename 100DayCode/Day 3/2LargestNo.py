""" Find two largest numbers from an array. """


l=list(int(x) for x in input("enter number seperated by space : ").split())
max=list(l[:2])
if max[0]<l[1]:
     max[0]=l[1]   # "this if condition sort the list element so that max[0]>max[1]""" 
     max[1]=l[0]
counter=0
for x in l[2:]:
     counter+=1          #tell how many time loop will be excute
     if x>max[0]:        #give True if x is greater than max list
          temp=max[0]    #this line manupulate max list and make the largest at
                         #second largest postion and x in lagest postion"""      
          max[0]=x
          max[1]=temp
print("first largest : {}\nSecond largest : {}".format(max[0],max[1]))
