with open("exixtingfile.txt", 'a') as file:
    file.write("\nParu")

with open("exixtingfile.txt","r") as file:
    content = file.read()
    print(content)