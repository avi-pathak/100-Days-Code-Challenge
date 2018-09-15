import os
def test():
	l = input()
	if os.path.exists(l):
		with open(l,'r') as f:
			rea= f.read()
			print(rea)
	else:
		print("File Does Not Exist")
