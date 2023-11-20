#Exception
#abnormal event during the execution of a program, but it can be handled

#Error or bug -> specific code -> produced by dev, its difficult to overcome

print("Insert the card")

try:
    a = 10/0
except Exception as e:
    print("Error/:",e)

print("Take your card")