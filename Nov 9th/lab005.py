#Use the properties,variables and method of your base class or parent class by the subclass -> Inheritance

#single inheritance
class Father:
    bank_bal = 100

    def one_bhk(self):
        print('Use it son')

class Son(Father):
    pass

s = Son()
s.one_bhk()

print(s.bank_bal)