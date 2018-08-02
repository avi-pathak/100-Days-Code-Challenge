class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

avi = Person("Avinash")
print("%s name is %s" % (Person.name, avi.name))
nic = Person()
nico.name = "Nic"
print("%s name is %s" % (Person.name, nico.name))
