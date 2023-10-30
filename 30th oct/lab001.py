
#List is mutable it can be changed
my_list = [1,2,3,4,5]
my_list[1] = 45
print(my_list)
print(type(my_list))
#Tuple


#tuple is immutable it is impossible to change
car = ("ford","audi",'range rover')
car2 =("ford","true","true")
print(type(car))
#car[1] = "tata"
print(len(car))
print(car2)

#list can be converted
list1 = [1,2,3,4,5]
print(tuple(list1))