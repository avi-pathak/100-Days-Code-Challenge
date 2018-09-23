class Employee:
	def __init__(self,empName,empSal,EmpNo):
		self.ename = empName
		self.esal = empSal
		self.eno = EmpNo
	def display(self):
		print("Employeename = ",self.ename,"Employee Number",self.eno,"Employee Sallery",self.esal)

