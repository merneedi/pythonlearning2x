given_year = 2024

#is_leap_year = False

if (given_year%4 ==0 and given_year%100 != 0) or (given_year %400 ==0):
    is_leap_year = True
else:
    is_leap_year = False

print(f"{given_year} is {is_leap_year}")