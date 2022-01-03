# CLASSES:
# SELF AND INIT FUNCTION

class Employee:
    no_of_leaves = 8
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee()
rohan = Employee()

harry.name = "Harry"         #This is waste of time writing each and every time name salary we can sort it in just one line.
harry.salary = 334
harry.role = "Instructor"      #here we are using without init function


rohan.name = "Rohan"
rohan.salary = 332
rohan.role = "Manager"


print(harry.printdetails())


# ----------------------------OR--------------------------------------

"""this is more easy way by using init function
 we don't have to specify each things like name salary role every time 
 we can give it just once and rest program could handle every thing very easily."""
class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."

harry = Employee("Harry", 2334, "Instructor")  #these arguments are handled by init function thus it is very helpful
rohan = Employee("Rohan", 2222, "Manager")

print(harry.printdetails())