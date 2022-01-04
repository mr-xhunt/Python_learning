# Multiple Inheritence
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



class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        return f"The Name is {self.name} and Game is {self.game}"
    
class CoolProgrammer(Employee, Player): #Multiple Inheritence 
    language = "C++"
    def printlanguage(self):
        return(self.language)

harry = Employee("Harry", 2334, "Instructor")  
rohan = Employee("Rohan", 2222, "Manager")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", 2345, "CoolProgrammer")

print(karan.printlanguage())