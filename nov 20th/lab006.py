#collection - list, dic, tuple, set, ordered dict

#Advanced collection - counter, ordereddict, userdict, deque,namedetuple etc

from collections import namedtuple

Person = namedtuple('Person',['name','age','gender'])
person = Person("Sandy",25,"M")
print("Name:",person.name)
print("Age:", person.age)
print("gender:", person.gender)

class Person2():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printMe(self):
        print(f"named details",{self.name})

person2 = Person2('Sandy', 26, "M")
person2.printMe()