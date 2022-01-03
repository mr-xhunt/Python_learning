# Class Method as Alternative Constructor

class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."
    
    @classmethod  #using classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))
#  we use these methods so that we dont have to use self in our function as if we use any such thing which is not used then it can be laggy for the progaram
   
   
    @staticmethod #why to put this code in class : So that this function can only be used by Employees
    def printgood(string):
        return ("This is good " + string)

harry = Employee("Harry", 2334, "Instructor")  #these arguments are handled by init function thus it is very helpful
rohan = Employee("Rohan", 2222, "Manager")
karan = Employee.from_str("Karan-3455-Director")



print(karan.printgood("Karan"))