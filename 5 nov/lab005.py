numbers_tuple = (1,2,3,4,5,6,7,8,9,10)

def is_even(num):
    return num % 2 ==0

even_num_tuple = tuple(filter(is_even,numbers_tuple))
print(even_num_tuple)

print(even_num_tuple[3])

l = [(1,23),(34,67)]
print(l)
print(l[0][0])
print(l[0][1])
