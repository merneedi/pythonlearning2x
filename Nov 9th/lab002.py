class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if name == "John":
            print("Dont set the name")
        else:
            self.__name

    def print_details(self):
        print('Your details are', self.__name,self.__age)


person = Person("SANDY", 25) #It will call the __init__ with name.age
person.print_details()
#print(person.__name) private


person.set_name("John")

name = person.get_name()
print(name)

#How to change it get and set?
#Fetch -get
#set the value - Constructor
