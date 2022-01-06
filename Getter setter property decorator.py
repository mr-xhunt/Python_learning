class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property #we use this to set property to the attributes : to make something happen
    def email(self):
        if self.fname == None or self.lname == None:
            return("Email is not set! Kindly set Your new Email using Setter!")
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter #this is setter used for changing values to the attributes already present in a reverse order
    def email(self, string):
        print("Setting.............")

        names = string.split("@")[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter #this is used to delete not exactly but to set the value of the attribute to none
    def email(self):
        self.fname = None
        self.lname = None

hindustani_supporter = Employee("Hindustani", "supporter")
nikhil_raj_pandey = Employee("Nikhil Raj", "Pandey")

print(hindustani_supporter.email)
hindustani_supporter.email = "This.that@codewithharry.com" #we used setter to handle this problem
print(hindustani_supporter.email)
del hindustani_supporter.email
print(hindustani_supporter.email)