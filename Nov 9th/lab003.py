class Password:

    def __init__(self, password):
        self.__password = password

    def get_password(self,isAuth):
        if isAuth:
            return self.__password
        else:
            print('Error')

    def set_password(self,password):
        if len(password) > 10:
            self.__password = password
        else:
            print("weak pwd")

    def print_details(self):
        print("Your pwd details", len(self.__password))

pwd = Password("hackerank")
pwd.print_details()

pssd = pwd.get_password(True)
print(pssd)

pwd.set_password('eihfefuehfl')
pwd.print_details()