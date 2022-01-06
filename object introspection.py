
#OBJECT INTROSPECTION

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return("Email is not set! Kindly set Your new Email using Setter!")
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter 
    def email(self, string):
        print("Setting.............")

        names = string.split("@")[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill", "F")

# print(skillf.email)
print(type(skillf))  #this is object introspection from where does it come

print(id("this is new world"))
print(id("this"))  #tells us the id for the things stored in the python

o = "thus a new world" #dir tells what can we do with this shit of things
print(dir(skillf))
print(dir("o"))

# import inspect
# print(inspect.getmembers(skillf))