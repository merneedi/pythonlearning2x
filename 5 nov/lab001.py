numbers = [1,2,3,4,5,6,7,8,9,10]
#num%2 ==0
even_numbers = [2,4,6,8,10]

# filter -> Number element can be less or equal the list

def is_even(num):
    return num % 2 == 0

op = is_even(20)
print(op)

even_numbers2 = filter(is_even,numbers)
even_numbers3 = map(is_even,numbers)
print(even_numbers3)
print(even_numbers2)
even_numbers_list = list(even_numbers2)
even_numbers_lists = list(even_numbers3)
print(even_numbers_lists)
print(even_numbers_list)