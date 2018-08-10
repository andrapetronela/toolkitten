# # Reading and writing files

# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")
# file = open(filename, encoding="utf8")
# raw = file.read()
# raw = raw.lower()
# # print(raw)

# def myFunction():
#     letters = []
#     result = []
#     for letter in raw:
#         if letter.isalpha():
#             if letter in letters:
#                 pass
#             else:
#                 letters.append(letter)
#     letters.sort()
#     for letter in letters:
#     	result.append([letter, raw.count(letter)])
#     print("result = " , result)
# myFunction()

#fix the above so it prints only A-Z and a-z

# for i in range(1, 123):
# 	if chr(i).isalpha():
#    		print(i, " stands for ", chr(i))

# Make a function that prints A-Z and a-z

# def alphabet():
# 	for i in range(1, 123):
# 		if chr(i).isalpha():
#    			print(i, " stands for ", chr(i))

# alphabet()

#Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;)

# phrase = input("Type your biggest wish. \n")
# result = []
# def my_function():
# 	for letter in phrase:
# 		result.append(ord(letter))
# 	print(result)
# my_function()


# Write a function that prints out all elements of the above board, starting from the first element 
# of the first line, till the end. Each line should be read from beginning to end.
# Calculate the size of a continent you are standing on in your 11 x 11 world in Civilization III.
# M = "land"
# o = "water"
# world = [
#  [M,o,o,o,o,o,o,o,o,o,M],
#  [M,o,o,o,M,M,o,o,o,o,M],
#  [M,o,o,o,M,o,o,o,M,M,M],
#  [M,M,M,M,o,o,o,o,o,M,M],
#  [M,o,o,M,M,M,M,o,o,o,M],
#  [M,o,o,o,M,M,M,M,o,o,o],
#  [M,o,o,M,M,M,M,M,M,M,o],
#  [M,o,o,M,M,o,M,M,M,o,M],
#  [M,M,o,o,o,o,M,M,o,o,M],
#  [M,M,o,o,o,M,o,o,o,o,M],
#  [M,o,o,o,o,M,o,o,o,o,M]]


# # def my_function():
# #  	for i in world:
# #  		for j in i:
# #  			print(j)
# # my_function()

# # def reverse_world():
# # 	for i in reversed(world):
# # 		for j in reversed(i):
# # 			print(j)
# # reverse_world()


#There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)

# def continent_counter(world, x, y):
# 	if x in range(11) and y in range(11):
# 		if world[y][x] != "land":
# 			return 0
# 		size = 1
# 		world[y][x] = "counted land"
# 		size = size + continent_counter(world, x-1, y-1)
# 		size = size + continent_counter(world, x , y-1)
# 		size = size + continent_counter(world, x+1, y-1)
# 		size = size + continent_counter(world, x-1, y )
# 		size = size + continent_counter(world, x+1, y )
# 		size = size + continent_counter(world, x-1, y+1)
# 		size = size + continent_counter(world, x , y+1)
# 		size = size + continent_counter(world, x+1, y+1)
# 		return size
# 	else:
# 		return 0
# print(continent_counter(world, 5, 5))

# Random Continent generator
# import random

# water = "o"
# land = "M"
# random_values = [water, land]

# def random_continent(n):
# 	my_continent = []
# 	for i in range(n):
# 		my_continent = [[random.choice(random_values) for i in range(n)] for j in range(n)]
# 	print("my_continent = ", my_continent)
# random_continent(12)



#Modify "a" for another name in my_dict. 
#Hint: you will have to create a new key-value pair, 
#copy in the value, and then delete the old one.

# my_dict = {
# 	"a": 35000,
# 	"b": 8000,
# 	"z": 450
# }

# my_dict["alpha"] = my_dict["a"]

# del(my_dict["a"])
# print(my_dict)



# Alice_in_wonderland - result in a dictionary


# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")
# file = open(filename, encoding="utf8")
# raw = file.read()
# raw = raw.lower()
# # print(raw)

# def myFunction():
#     letters = {}
    
#     for letter in raw:
#         if letter.isalpha():
#             if letter in letters:
#                 pass
#             else:
#                 letters[letter] = raw.count(letter)
#     # for letter in letters:
#     # 	result.append(letter, raw.count(letter))
#     print("result = " , letters)
# myFunction()



#Create a dictionary with your own personal details, feel free to be creative and funny
# so for example, you could include key-value pairs with quirky fact, fav quote, pet. 
# Practice adding, modifying, accesing

# about_me = {
# 	"name": "Andra",
# 	"birth_year": 1989,
# 	"fav_socks_color": "yellow",
# 	"age": "Can you guess it? :)",
# 	"hobby": "Crochetting a code",
# 	"fav_drink": "Always... Coca&Cola",
# }

# about_me["motto"] = "!problem solved == !sleep"

# about_me["age"] = "Mind your own code :D"

# print(about_me["fav_drink"])

# print(about_me)


#Review the chat reply of today's beautiful class interaction and instantiate 
# a student variable for everyone who shared their dream.

# class Student():
# 	def __init__(self, name, discord_id, dream, fav_food):
# 		self.name = discord_id
# 		self.discord_id = name
# 		self.dream = dream
# 		self.fav_food = fav_food
# 	def my_print(self):
# 		print(self.name + self.discord_id + self.dream + self.fav_food)

# s1 = Student("Andreea", "Andreea[Gold]", "University Teacher", "Wontonmee")
# s2 = Student("Virginia Balseiro", "Virginia", "Moving to Europe", "Pasta")
# s3 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "Being an amazing developer", "Pasta")
# s4 = Student("Alter edco", "alterdeco[Gold]", "Travelling", "Soup")
# s5 = Student("Jessica", "Jessi_RS[Gold]", "Getting a job as a developer by the end of the year", "Pasta")
# s6 = Student("Sacha Young", "sacha[Gold]", "returning to researching", "french fries")
# s7 = Student("Marwa Qabeel", "Marwa Qabeel[Gold]", "data analyst", "pasta")


# s1.my_print()

# class Student():
# 	def __init__(self, first_name, last_name, tel_no, email, github_name, location, gender, coding_level,
# 		techno_skills, studies, background, employment_status, aim):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.tel_no = tel_no
# 		self.email = email
# 		self.github_name = github_name
# 		self.location = location
# 		self.gender = gender
# 		self.coding_level = coding_level
# 		self.techno_skills = techno_skills
# 		self.studies = studies
# 		self.background = background
# 		self.employment_status = employment_status
# 		self.aim = aim