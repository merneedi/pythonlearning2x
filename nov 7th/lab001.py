class Car:
    name = "Sanddeep" #class variable


# Constructor
    def __init__(self):#default cons
         print('I will be called first ->' + self.name)


    def start_engine(self):
         print('Starting a car')


car1_objref = Car()
car2_objref = Car()

print(id(car1_objref))
print(id(car2_objref))

# Object is created a special function is called automatically __int__()
# All the attribute object you can intialize - add some inital value to them
