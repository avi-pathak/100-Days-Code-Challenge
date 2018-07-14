def binSearch(l,n):
        end=len(l)
        beg=0
        mid=(0+end)//2
        print(mid)
        while(beg <= end):
                if l[mid]==n:
                        return mid
                elif n<l[mid]:
                        end=mid-1
                else:
                        beg=mid+1
                mid=(beg+end)//2
        return None
l=[10,20,30,40,50,60,70,80,100,200,300,100,400,500]
n=int(input("Enter the element to be searched "))
item=binSearch(l,n)
if item==None:
        print("Not Found")
else:
        print("Found At ",item)
