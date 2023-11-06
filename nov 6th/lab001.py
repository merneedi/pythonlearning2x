# class and objects in python

#person
#attributes - name,age
#methods - can do -> run(), sleep()

class Person:
    #attributes
    name =None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    #methods
    def talk(self):
        print("talk")

    def sleep(self):
        print('sleep')

    def walk(self):
        return ('walk')

amit_obj = Person()
amit_obj.name = 'Amit'
amit_obj.age = 56
amit_obj.sleep()
print(amit_obj)

kiran_obj = Person()
kiran_obj.name = 'kiran'
kiran_obj.age = 45
print(kiran_obj)
kiran_obj.talk()
kiran_obj.walk()