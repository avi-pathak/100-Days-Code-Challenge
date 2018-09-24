class Employee:
     city='GhaziaBad'
     def __init__(self,name,sal):
          self.name = name
          self.sal = sal
     @classmethod
     def m1(cls):
          cls.country='India'
     @staticmethod
     def m2():
          Employee.org='Kiet'
t=Employee('Avinash',1000)
t.m1()
t.m2()
print(t.__dict__)#give dict of all instace variable of object

print(Employee.__dict__)#give all elemnt of class in form of dict

print(t.city,t.country,t.org)#by using the object we can only access static variable 

print(Employee.city,Employee.country,Employee.org)#by jusing class name we can access and modify the valu of static variable
