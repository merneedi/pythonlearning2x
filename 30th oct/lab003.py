tuple3 = tuple(["sandy", "lucky"])
print(tuple3)
print(tuple3[1])

team1 = ("rohit",'stark')
team2 = ("virat", "bumrah")
output = team1 + team2
print(output)

my_tuple = (1,2,3,4)
print(list(my_tuple))

my_list = [1,2,3,4]
print(tuple(my_list))

x = 10 #value assigns to variable
a,b =34,56 #multiple values assigns to variables
s,f,t = (54,65,6) #tuple assigns to multiple variables
print(s)
print(f)
print(t)

#Nested tuple
eam1 = ("rohit",'stark')
team2 = ("virat", "bumrah")
output = (team1 , team2)
print(output)
print(output[0][1])
print(output[1][0])

#search in tuple
cities = ('moscow',"kkd", "pdp",'paris')
print("paris" in cities)
