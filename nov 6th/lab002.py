# self is a special variable that is used within the context of oop
# It is a refernce to the instnce of the class
# Access and manipulate the attributes and methods of that instance/object

class Car:
    name = None
    color = None
    engine = None
    speed = None
    model = None

    def start_engine(self):
        print('Engine is started')

    def drive(self):
        print('Drive')

    def car_brake(self):
        print("Brake")

    def who_is_driving(self):
        print("I am driving -> " + self.name)


tesla_obj_ref = Car()  # this is instance of a class-object
rover_obj_ref = Car()  # this is instance of a class-object

tesla_obj_ref.name = "Tesla"
rover_obj_ref.name = "Range rover"

print(tesla_obj_ref)
print(rover_obj_ref)

tesla_obj_ref.who_is_driving()
rover_obj_ref.who_is_driving()
