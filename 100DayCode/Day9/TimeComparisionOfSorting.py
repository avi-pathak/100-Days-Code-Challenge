print("PROGRAM TO CHECK SORTED ARRAY WHTHER IT IS SORTED OR NOT")
print()
print("the size of the input is 100k")
print()
def sort():
     flag=False
     t1=t.clock()
     for i in range(len(l)):
          for j in range(len(l)-i-1):
               if l[j] > l[j+1]:
                    flag=True      #this line tell us if this section is not being excuted
                    l[j],l[j+1]=l[j+1],l[j] #swapping the next elemnt is less than it left element
         # if(flag == False):
          #     print("Already Sorted")
           #    break
          '''this Method is Not optimized Bcoz Nomatter Array is already
                    sorted Or Not it will run N*2
                    But Wecan Optimized it we can take a flag check the very first inner loop if there is
                    no swapping happend that mean our list has already sorted 
                    '''
     t2=t.clock()
     print("By Typical Bubble sort")
     print("O(N^2) Time",t2-t1)
def sort1():
     flag=False
     t1=t.clock()
     for i in range(len(l)):
          for j in range(len(l)-i-1):
               if l[j] > l[j+1]:
                    flag=True      #this line tell us if this section is not being excuted
                    l[j],l[j+1]=l[j+1],l[j] #swapping the next elemnt is less than it left element
          if(flag == False):
               print("Already Sorted")
               break
          '''this Method is Not optimized Bcoz Nomatter Array is already
                    sorted Or Not it will run N*2
                    But Wecan Optimized it we can take a flag check the very first inner loop if there is
                    no swapping happend that mean our list has already sorted 
                    '''
     t2=t.clock()
     print("By Optimized Bubble sort")
     print("o(N) Time",t2-t1)

sort()
sort1()

