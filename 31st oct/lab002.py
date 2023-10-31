#If you have duplicate key, latest value of key will be used

dict = {'a':12, "b" :56, "c":566, "a":45}

print(dict)
print(dict.keys())
print(dict.values())
keys = list(dict.keys())
values = list(dict.values())
print(keys)
print(values)
print(keys[0])
print(dict.items())
set_dic = set(dict.items())
print(set_dic)

