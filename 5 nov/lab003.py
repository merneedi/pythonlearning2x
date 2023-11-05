products = [
    {"name": 'Laptop', 'price': 1000},
    {'name': "smartphone", "price": 500},
    {'name': 'tablet', 'price': 300},
    {'name':"headphones", 'price': 100}
]

print(type(products))
print(type(products[0]))

def is_affrodable(item):
    return item["price"] < 500

affordable_items = list(filter(is_affrodable,products))
print(affordable_items)
print(affordable_items[0]['name'] + " " + str(affordable_items[0]["price"]))

for i in affordable_items:
    print(i['price'],i['name'])