#F,M = Multlevel = son

class Father:
    def father_money(self):
        return "5"

class Mother:
    def mother_money(self):
        return "5"

class Son(Father,Mother):
    pass

s = Son()
print(s.father_money())
print(s.mother_money())