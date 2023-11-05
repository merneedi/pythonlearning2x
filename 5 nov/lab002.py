#Map will have  exectuing the function on every element

words = ["apple", "banna", 'strawberry',"mango", "fig"]
min_length = 5

def check_length(word):
    return len(word) > min_length

op = check_length(words[2])
print(op)

op2 = list(filter(check_length,words))
print(op2)