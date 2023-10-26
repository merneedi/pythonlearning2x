s = 12345
m = s%10
v = int(s/10)
print(m)
print(v)

num = int(input("Enter the num\n"))

sum = 0
while num != 0:
    digit = num%10
    sum = sum + digit
    num //= 10
print(sum)