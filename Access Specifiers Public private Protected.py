class Employee:
    no_of_leaves = 9 #this is public specifiers

    _var = 234 #this is public protected specifiers

    __var2 = 2345 #this is private specifiers


    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."

harry = Employee("Harry", 2334, "Instructor")  #these arguments are handled by init function thus it is very helpful
rohan = Employee("Rohan", 2222, "Manager")

print(harry._var) #you may find that public protected specifiers can be printed but it cannot be accessed by any third party class
#it can only be printed by the class in which it is or its lineage class

# print(Employee.__var2) by this method it can never be printed , it can only be printed by adding  class name with underscore before the class name :
#  
print(harry._Employee__var2) #also known as name mangling in python

