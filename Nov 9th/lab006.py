#Multilevel inheritance

#level -> gf - f- son

class Grandparent():
    def grandparent_method(self):
        return 'Grandparents method'

class Parent(Grandparent):
    def parent_method(self):
        return 'parent method'

class Child(Parent):
    def child_method(self):
        return 'child method'

child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
