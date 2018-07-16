Pattern-8:
-----------------
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A
------------------------------
 n=int(input("Enter the number of rows: "))
 for i in range(1,n+1):
  for j in range(1,n+1):
    print(chr(65+n-i),end=" ")
  print()
