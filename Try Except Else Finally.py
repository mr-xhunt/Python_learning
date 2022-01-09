# try except else finally

f1 = open("maya.txt")

try:
    f = open("does.txt")

except Exception as e: #we can write as many except for diffrent errors
    print(e)

else: #this will run only if except is not running : either except will run or else will
    print("Hello world")

finally:       #This will be completed any how either there is exception or else condition no matter,
    # this is used to handle all mess caused while try like closing files which is opened
    print("Run this anyway")
    # f.close
    f1.close
print("Important Stuff") #even if file doesn't exist then also the important stuff run due to try and except