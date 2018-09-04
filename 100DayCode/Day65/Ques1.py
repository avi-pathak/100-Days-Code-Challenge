def banker(pro,done,alloc,avail,maxreq,m,n):
     need=[[-1 for i in range(n)]for i in range(m)]



     for i in range(m):
          for j in range(n):
               need[i][j]=alloc[i][j] - maxreq[i][j]
               need[i][j] = -1 * need[i][j] if need[i][j] < 0 else need[i][j]

     print()

     print("This Will Be The safe Sequece")

     print()

     while any(done[i] == False for i in range(len(done))):       # Frome Safty Algo from Banker Algo
          for i in range(m):
               if all(need[i][j] <= avail[j] for j in range(3)) and done[i] == False:
                    for j in range(len(avail)):
                         avail[j]+=alloc[i][j]
                    print("",pro[i],end=' ')
                    done[i] = True
m,n=5,3
pro=['p0','p1','p2','p3','p4']
done=[False for i in range(m)]
alloc=[[0,1,0],
       [2,0,0],
       [3,0,2],
       [2,1,1],
       [0,0,2],
     ]
maxreq=[
          [7,5,3],
          [3,2,2],
          [9,0,2],
          [2,2,2],
          [4,3,3],
     ]

avail=[3,3,2]


banker(pro,done,alloc,avail,maxreq,m,n)
