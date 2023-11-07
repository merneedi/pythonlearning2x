class Car:
    name = "Sanddeep" #class variable


# Constructor
    def __init__(self,make,model):#default cons
         self.make = make, #instance variable closely related to objects
         self.model = model #instance variable
         print('I will be called first ->' + self.name)


    def start_engine(self):
         print('Starting a car', self.make, self.model)


car1_objref = Car("rangerover",'x5')
car2_objref = Car('rollsroyce','phantom')

car1_objref.start_engine()
car2_objref.start_engine()

print(id(car1_objref))
print(id(car2_objref))

#object is created to call the constructor

