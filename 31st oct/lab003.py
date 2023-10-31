a = {1,2,3,4,4,5,3}
print(type(a))
b = set([1,2,3])
print(type(b))

my_dict = {'a' : 1, "b" :2}

val = my_dict.pop("a")

print(val)
print(my_dict)

#API testing => Json we can use dict which is similar data type as Json
print(dir(dict()))

cities = {"hyd": "manikonda", "Banglore":"mysore"}
print(len(cities))

for i,j in cities.items():
    print(i,j)
    #print(j)