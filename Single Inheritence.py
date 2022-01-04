# Single Inheritence
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
    
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod 
    def printgood(string):
        return ("This is good " + string)

# here programmer class is inheriting from parent class Employee
# this is single Inheritence  

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        super().__init__(aname, asalary, arole)  #super helps to increase code reusability and this is known as overriding( we can also again type self.name etc)
        self.languages = languages
    def printprog(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role} and He knows {self.languages}."

harry = Employee("Harry", 2334, "Instructor")  
rohan = Employee("Rohan", 2222, "Manager")

karan = Programmer.from_str("Karan-3455-Programmer-[Python, Java, C, C#]")
shubham = Programmer("Shubham", 5555, "Programmer", ["Java", "Python", "C++"])

print(shubham.printprog())