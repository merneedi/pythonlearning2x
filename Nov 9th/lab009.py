#Hybrid inheritance
#multiple type of inheritance, such as single, multiple and multilevel inheritance
#mro (method resolution order) first comes first
class A:
    def methodA(self):
        return "methodA"

class B(A):
    def methodB(self):
        return 'methodB'

class C(A):
    def methodC(self):
        return 'methodC'

class D(B,C):
    def methodD(self):
        return "methodD"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())