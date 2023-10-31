#popitem is used to remove and return arbitary key value pair from the dict
my_dict = {"a" :1 , "b" : 2, "c" : 3}
val = my_dict.popitem()
val2 = my_dict.pop('a')
print(val2)
my_dict['a'] = val2
print(my_dict)
print(val)
#del my_dict
print(my_dict)