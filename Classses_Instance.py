# classes - template
# object - Instance of the Class

# OOPS work on DRY rules
# DRY - Don not repeat Yourself

# Creating Our first Class in Python

class Student:
    no_of_holidays = 8
    pass

Harry = Student()
Mayank = Student()

Harry.name = "Harry Pandey"
Harry.std = 12
Harry.sec = "A"

Mayank.name = "Mayank Kumar Choubey"


print(Harry.sec)
print(Mayank.name)


print("No. of holidays for mayank is ", Mayank.no_of_holidays)
print(Mayank.__dict__)

Mayank.no_of_holidays = 9
print(Mayank.__dict__)
print(Mayank.no_of_holidays)
print(Student.__dict__)