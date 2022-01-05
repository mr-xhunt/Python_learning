class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):  #created add method dundar method to override overloading
        return self.salary + other.salary

    def __repr__(self): #use this to make print harry look beautiful
        return f"Employee: [{self.name}, {self.salary}, {self.role}]"
    
    def __str__(self): #if str is present then print harry will give from str and to specially call return of repr we need to call repr
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."
harry = Employee("Harry", 2334, "Instructor")
rohan = Employee("Rohan", 2222, "Manager")

print(harry + rohan)
print(harry) 
print(repr(harry))