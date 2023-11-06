#Take input from user
#methods cant call the func directly

class Car:
    color: None
    model :None

    def car_details(self):
        print("Your details are " + self.color, self.model)


car_color = input('Enter the car color\n')
car_model = input('Enter the car model\n')

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

#obj ref we can call the function
car_obj_ref.car_details()

