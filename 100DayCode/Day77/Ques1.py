"""Writing the binary file"""

f=open("racecar.png","rb")

f2=open("file2.png","wb")

bytes=f.read()

f2.write(bytes)

print("Binary file copied successfully")
f.close()
f2.close()
