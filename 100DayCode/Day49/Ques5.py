''n this Question Just Need to use to funtion of numpy So easy''
import numpy
m,n=list(map(int,input().strip().split()))
l1=[]
for _ in range(m):
    l=list(map(int,input().strip().split()))
    l1.extend(l)
arr=numpy.array(l1)
arr=numpy.reshape(arr,(m,n))
print(numpy.transpose(arr))
print(arr.flatten())



