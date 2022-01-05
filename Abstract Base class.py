# Abstract Base class

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC): #here this abc implements that printarea is neccessary to put into all of the classes
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())