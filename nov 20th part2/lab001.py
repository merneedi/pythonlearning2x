#File handling
#How to read a text,write into it using python code
#file_obj.readline(),readlines(),write(),writelines(),close()

try:
    with open("Textdata2.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(e)