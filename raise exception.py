
a = input("What is your name")

b = input("How much do you earn")
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")  #raising exception at early stage so that we dont want to use resources if user typed to error

print(f"hello {a}")

#1000 lines taking 1 hour

#using valueerror to block a user
c = input("Enter your name  ")

try:
    print(f)

except Exception as e:
    if c =="harry":
        raise ValueError("Harry is blocked, he is not allowed")

    print("Exception Handled")


