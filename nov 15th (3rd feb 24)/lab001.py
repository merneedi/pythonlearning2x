# Exception

# abnormal event during the execution program, but it can be handle

# Error - Specific code -> 1 gb -> 1.2 gb ? stackoverflow

# 10,12 - Error -> It is very difficult to overcome

# Memory error - Error -> Restart, retry

print("Start")

try:
    # Code which you think can you give exception
    a = 10/0
except ZeroDivisionError:
    print("Your are doing division with zero")


print("End")
