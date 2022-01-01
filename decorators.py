# Let's learn Decorators in python
# this is used when we need to use one single work to perform over many function then this is very helpful
def dec1(func1):
    def exec():
        print("Executing Now----------------------------------------------------")
        func1()
        print("Executed!")
    return exec

@dec1
def max():
    print("port 80 hacked\nport 23 hacked\nport 22 error")

# max = dec1(max)

max()