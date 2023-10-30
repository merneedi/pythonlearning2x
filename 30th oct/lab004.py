#set can't be change but it shouldnt have duplicates and unordered collection of elements
set1 = set()
print(set1)
set2 = set("sandy")
print(set2)
set3 ={1,2,3,4,5,5}
set3.remove(2)
#set3[1] =5
print(set3)
print(type(set3))

set12 = set(["sandy", 'for', 'lucky'])
print(set12)

for i in set12:
    print(i, end=' ')
t = ('testing', "for", 'testing')
print('\n set with the use of tuple:')
print(set(t))