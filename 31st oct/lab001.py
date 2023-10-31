#A dictionary is an ordered collection of data in key-value pair format
# set stores value {}
#dict {} keys and values, name => lucky
s1 = {}
s2 = dict()
print(type(s1))
print(type(s2))
#Dict =>  similar to JSON

Dict = {"Rameesh": 967509659, "Rahim"  : 94857685043,"ganesh":5767549}

print(Dict)
print(len(Dict))
#print(Dict[0]) here you can access key element only
print(Dict['Rameesh'])

phone_book = dict(Batman =123, superman=345, wonder =678)
print(phone_book)
print(phone_book['wonder'])
print(phone_book.get("wonder"))

sandy_details = dict(name = 'sandy', age = "25", ismale = True, Address = 'kkd')
print(sandy_details)

lucky_details = {"name": "lucky", "34":56.8, "isfemale": True}
print(lucky_details.get('34'))
#key should be string