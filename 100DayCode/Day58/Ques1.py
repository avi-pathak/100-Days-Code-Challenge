def descending(l):
  return all(l[x-1]>=l[x] for x in range(1,len(l)))
