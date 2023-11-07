class Person:
    def __init__(self,name):
        self.name = name
        print('You created an object')

    def printDetails(self):
        print('Your details are ', self.name)

    def printDetails2(self):
        print('Your details are', self.name)

amit = Person("Amit")
amit.printDetails()
Nihil = Person("Nikhil")
Nihil.printDetails2()

#In python we have multiple constructors but we have to call single constrcutor