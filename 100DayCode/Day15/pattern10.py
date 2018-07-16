Pattern-10:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
------------------------------
Code - 1:
----------------
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end=" ")
   print()
------------------
Code - 2:
-------------
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
print("* "*i)
