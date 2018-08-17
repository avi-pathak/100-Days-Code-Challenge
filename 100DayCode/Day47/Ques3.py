'''
in this Question we just need to find the correct u=index of marks and summing up the value of marks in dexhave a look and think
for a while u will understand every thing
'''
from collections import namedtuple
n=int(input())
column=list(input().split())
mark_index,sum=column.index("MARKS"),0
for _ in range(n):
    info=list(input().split())
    sum+=int(info[int(mark_index)])
print(sum/n)
