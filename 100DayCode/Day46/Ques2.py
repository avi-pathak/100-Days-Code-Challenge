'''groupby function read a string or any sequce and make the group of consecutive element and it key which accour in consecutive manner

for example
for string 1222311 gruop return k , v wher k is the key and v is the list for element of of its consecutive for more 
clarification see below the example
it will return for 1222311
1 [1]

2 [2,2,2]

3 [3]

1 [1,1]

as it shows we just need to print the each key and ite group length python made it So Simple 
'''


from itertools import groupby
num=[]
freq=[]
string=input().strip()
for i,j in groupby(string):
    num.append(i)
    freq.append(list(j))


for i in range(len(num)):
    group_length=len(freq[i])
    key=int(num[i])
    print(tuple((group_length,key)),end=' ')
    
