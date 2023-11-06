# method is used in class and function is used everywhere

class Myclass:

    def print_my_name_with_last_name(self,name, last_name, age):
        print("You name is -> " + name, last_name, age)


sandy_obj_ref = Myclass()
#sandy_obj_ref.name = "sanddeep"

sandy_obj_ref.print_my_name_with_last_name(name="surya",last_name="dutta", age=25)