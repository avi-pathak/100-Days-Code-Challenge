from zipfile import *

f=Zipfile("files.zip","w")

f.write("file1.txt")

f.close()
