import csv

from dir import mod2
mod2.greet("sandy")

person = mod2.Person("Sann")
person.intro()

with open("testdata.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            print(value, end=" ")
        print()

    #with statement is used to open the file and it is automatically handles te closing of the file, ensuring the resources are properly released

    #when youre done reading the file