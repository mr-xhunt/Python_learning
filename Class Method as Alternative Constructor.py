# Class Method as Alternative Constructor

class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."
    
    @classmethod  #using classmethod when we don't want self to automatically takes place in our function we use classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    # we can write this one liners when we got a text file where name salary role are stored
    #  with dash or hyphen or slash or any thing we can use split here get our result
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-") 
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

harry = Employee("Harry", 2334, "Instructor")  #these arguments are handled by init function thus it is very helpful
rohan = Employee("Rohan", 2222, "Manager")
karan = Employee.from_dash("Karan-3455-Director")

Employee.change_leaves(32)

print(karan.printdetails())
