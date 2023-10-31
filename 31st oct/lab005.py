#ordered dict
#slicing is use only for list items
#dict - It will not keep the order of insertion
#orderdict - It will keep the order of insertion
from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od["d"] = 56
od["c"] = 45
od["b"] = 43
print(od)

keys = list(od.keys())
print(keys)
keys_sort = sorted(keys)
keys_rev = list(reversed(keys_sort))
print(keys_rev)
print(keys_sort)

od2 = OrderedDict()
od2[keys_sort[0]]= 451
od2[keys_sort[1]]= 566
od2[keys_sort[2]]= 433
od2[keys_sort[3]]= 978
print(od2)
keys2 = list(od2.keys())
keys_sort_rev = sorted(keys2, reverse = True)

print(keys_sort_rev)



