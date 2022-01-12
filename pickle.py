import pickle
#pickeling a python object
cars = ['Audi', 'BMW', 'Jaguar', 'Lamborghini']  #here this object could be anything tuple,list, variable etc

file = 'mycar.pkl'

fileobj = open(file, 'wb')
pickle.dump(cars, fileobj) #this takes file object
fileobj.close()


#de pickeling the file 

file = 'mycar.pkl'
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
fileobj.close()