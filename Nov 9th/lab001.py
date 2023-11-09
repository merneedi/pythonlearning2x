#Public - variable define as = Don't mention anything
#Protected - _ => out of module doesnt accepted
#Private - __

#variable and function

class BankAccount:

    def __init__(self):
        self.balance = 0 #Instance variable (acces only through object)

    def deposit(self,amount): #public function
        #self.balance = self.balance + amount
        self.balance += amount

    def _withdraw(self,amount): #protected
        self.balance -= amount

    def __showbalance(self): #private
        print("Your bal:" , self.balance)

    def is_Auth_True(self,isAuth): #public fun access (show balance) private func because it is in the class
        if isAuth:
            self.__showbalance()
        else:
            print("Your not auth")

    def do_withdraw_by_bank_manager(self,amount):
        self._withdraw(amount=amount)

jpmorgan_chase = BankAccount()

jpmorgan_chase.deposit(1000)
jpmorgan_chase._withdraw(499) #Not a good practise
#jpmorgan_chase.__showbalnce() #It cant access directly

#write the code to Auth- dev
jpmorgan_chase.is_Auth_True(False)

