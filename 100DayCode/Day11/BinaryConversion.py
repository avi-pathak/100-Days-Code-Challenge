l,num=[],int(input("enter the number"))
while num > 1:
     l.append(num%2)
     num=int(num/2)
l.append(1)
print("Binary Equivelenet------->",l[::-1])
