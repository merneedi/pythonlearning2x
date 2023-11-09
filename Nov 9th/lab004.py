# Parent -child
#FATHER - Son
#Single inhertance -> 90%

class Animal:

    def car(self):
        print('Lambo')

    def speak(self):
        print("Animal can speak!")


class Dog(Animal):
    def speak(self):
        print("Bow Bow")

    def i_want_drive(self):
        Animal().car()


AS= Animal()
AS.speak()

dog = Dog()
dog.speak()

dog.i_want_drive()