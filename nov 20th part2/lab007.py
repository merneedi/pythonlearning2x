import csv

temp_data = []
id_update = 2
new_age = 23

with open('cummins.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

temp_data[2][2] = 25

#for row in temp_data:
 #   if row[0] == id_update:
 #       row[2] = new_age

with open("cummins.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)