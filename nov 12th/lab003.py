#File to in python
#file = open('sandy.txt','r')
#print(file.read())
#file.close()

# Append
file2 = open("sandy.txt",'a') # increases means adding more
file2.write("Yes Yes") #append is adding
file2.close()

file3 = open('sandy2.txt','w') # it dosent add new data means overright
file3.write("No No")
file3.close()

file = open('sandy.txt','r')
print(file.read())
file.close()

try:
    file = open("Pramod.txt.",'r')
    print(file.read())
    #file.close()
except FileNotFoundError as vishal:
    print('File not found', vishal)
finally:
    if file:
        file.close()
