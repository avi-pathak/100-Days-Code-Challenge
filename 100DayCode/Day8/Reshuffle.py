'''Reshuffle a given array(array with all unique values, so no duplicate in array) in way so that, every odd(including 1 too) index should be larger than it's left and right.
Example: input : {1, 3, 5, 4, 8, 10} output: {1, 5, 3, 8, 4, 10}

here index 1, 3, 5, and so on are larger than it's left and right both.'''


l=[1, 5, 3, 8, 4, 10]
for x in range(1,len(l)-1,2):
     if l[x]<l[x+1]:
          l[x],l[x+1]=l[x+1],l[x]
print(l)
