set1 = {1,2,3,4}
set2 = {4,5,6,7}
out = set1.union(set2)
out2 = set1.intersection(set2)
out3 = set2.difference(set1)
subset = set2.issubset(set1)
print(subset)
print(out2)
print(out)
print(out3)

def func():
    name = "lucky"
    return name

def func2():
    name = 'sandy'

output = func()
output2 = func2()
print(output2)
print(output)