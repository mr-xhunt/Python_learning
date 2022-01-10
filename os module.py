# OS Module: within operating system if we wish to perform any work os module will be very useful

import os

print(os.getcwd())  #get current working directory
os.chdir("C://")    #change directory
print(os.getcwd())
f= open("maya.txt") 

print(os.listdir())    #list all directory
print(os.listdir("C://"))

os.mkdir("This")
os.makedirs("This/That") #making subdirectories
os.rename("maya1.txt", "maya.txt")
print(os.environ.get("Path"))  #get environment path


print(os.path.exists("C://Program Fiasf")) #check if any file exist or not
print(os.path.isdir("C://Program Files"))