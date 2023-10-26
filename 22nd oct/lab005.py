num = int(input("Enter the number\n"))
#fact =1
if num <0:
    print('factorial is not possible!!')
else:
    fact =1
    for i in range(1,num+1):
        fact = fact*i
    print('factorial of number is',fact)