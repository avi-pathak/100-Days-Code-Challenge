def orangecap(d):
  max= 0
  d1 = {}
  for i in d.keys():
    for j,k in d[i].items():
      if k > max:
        max  =  k
        d1.clear()
        d1[j] = k;
  for i in set(d1.items()):
       return i
