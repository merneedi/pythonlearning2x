#Hierachial inheritance
# son - father - daughter
class Vehicle:

    def info(self):
        return "This is vehicle"

class Car(Vehicle):

    def info(self):
        return "This is car"

class Bicycle(Vehicle):

    def info(self):
        return "This is Bicycle"

car = Car()
bic = Bicycle()

print(car.info())
print(bic.info())
