user_input = str(input('enter the name\n'))

rev_str = user_input[::-1]
print(rev_str)

def reverse_string(name):
    reverse = ''
    for char in name:
        reverse = char + reverse
    return reverse

result = reverse_string(user_input)

if user_input == result:
    print("Palindrome")
else:
    print("Not palindrome")

