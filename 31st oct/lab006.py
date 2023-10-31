my_dict = {"a":1, 'b':2,'C':3}
for k,v in my_dict.items():
    if v ==2:
        print("v is found")

op ="b" in my_dict
print(op)

dict = {True:123}
print(dict)
print(type(dict))
print(dict[True])