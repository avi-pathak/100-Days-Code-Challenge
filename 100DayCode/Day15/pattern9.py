Pattern-9:
------------------
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
---------------------------
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
  for j in range(1,n+1):
    print(chr(65+n-j),end=" ")
  print()
