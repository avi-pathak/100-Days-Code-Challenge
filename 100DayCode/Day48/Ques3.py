'''in this Question i got the chance to learn about the oprdercounter order counter simply count in order of sequence but remember for using 

for using orderd counter and deom class is mandatory'''

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
