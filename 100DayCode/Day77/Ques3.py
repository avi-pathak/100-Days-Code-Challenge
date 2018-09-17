from zipfile import *

f=ZipFile("files.zip","r")

names=f.namelist()
print()

for name in names:
     print("the name of the file is",name)

     print("the content of the file ")
     f1=open(name,"r")
     print(f1 .read())
#f.write("file1.txt")

f.close()
