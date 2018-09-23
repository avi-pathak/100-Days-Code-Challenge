import pickle
import emp

f=open("emp.dat","wb")
n=int(input("Enter the number of employee"))

for _ in range(n):
	name =raw_input("Enter the employee name")
	no = int(raw_input("enter the Employee NUmber"))
	sal = int(raw_input("Enter the Employee sallerry"))
	obj = emp.Employee(name,no,sal)
	pickle.dump(obj,f)
print("Pickling is done")
