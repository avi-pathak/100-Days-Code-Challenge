'''Using Collection Module'''

import collections as c
x = int(input())
shoe_size = list(map(int,input().split()))
n = int(input())
sell=0
d=dict(c.Counter(shoe_size))
for _ in range(n):
    key,Price=list(map(int,input().split()))
    if key in d.keys():
        if d[key]!= 0:
            sell+=Price
            d[key]-=1
print(sell)`

''' Using Simple List'''

x = int(input())
shoe_size = list(map(int,input().split()))
n = int(input())
sell = 0
for i in range(n):
    s, p = map(int,input().split())
    if s in shoe_size:
        sell = sell + p
        shoe_size.remove(s)
print(sell)
