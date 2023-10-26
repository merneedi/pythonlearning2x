n1 = float(input("enter n1\n"))
n2 = float(input("enter n2\n"))
n3 = float(input("enter n3\n"))

max_out = n1 if (n1>n2 and n1>n3) else(n2 if (n2>n3) else n3)

#print(max_out)
print(f"The max num of {n1},{n2} and {n3} is {max_out}")