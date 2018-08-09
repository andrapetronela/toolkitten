'''#hours in a year
print(24 * 365)

#minutes in a decade
print( ((60*24) * 365) * 10 )

#my age in seconds
print( ((3600 * 24) * 365) * 28)

#Andreea's age
print(48618000 / (( 3600 * 24) * 365))

# integer stored in a 32bites

#32-bit
 print(round(2**32 / 1000 / 60 / 60 / 24))

 #64-bit
 print(round(2**64 / 1000 / 60 / 60 / 24))


'''

# my age
# import datetime 

# birthDate = datetime.datetime(1989, 9, 20)
# now = datetime.datetime.now()
# print(now - birthDate)


#Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
#Finally, it should greet the person using their full name. 

# firstName = input("What is your first name?")
# middleName = input("What is your middle name?")
# lastName = input("What is your last name?")

# print("Welcome to Python, " + firstName + " " + middleName + " " + lastName)


'''Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
(Do be tactful about it, though.) '''
# favoriteNumber = int(input("What is your favorite number?"))
# suggestedNumber = favoriteNumber + 1
# print("We think you should consider " + str(suggestedNumber) + " as well.")


'''
Angry boss. Write an angry boss program that rudely asks what you want. 
Whatever you answer, the angry boss should yell it back to you and then fire you.'''
# print("What do you need?")
# employer = input()
# print("What do you mean you need " + employer + "?" + " You're fired!")


'''Write a program that will display a table of contents so that it looks like this: '''

# content = ["Chapter 1: Getting Started", "page 1", "Chapter 2: Numbers", "page 9", "Chapter 3: Letters", "page 13"]

# width = 40
# print("Table of Contents".center(width))
# print("-" * 40)

# col_width = 30

# i = 0
# while (i<len(content)):
# 	print(content[i].ljust(col_width), content[i+1].ljust(col_width))
# 	i+=2



'''- “99 Bottles of Beer on the Wall.”
 Write a program that prints out the lyrics to that beloved classic, 
“99 Bottles of Beer on the Wall.” '''


# i = 99
# while i > 0:
# 	print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer. \n"
# 		+ "Take one down and pass it around, " + str(i) + " bottles of beer on the wall.")
# 	print("\n\n")
# 	i-=1
# print("0 bottles of beer on the wall, 0 bottles of beer. \n"
# 	+ "Take one down and pass it around, 0 bottles of beer on the wall.")


'''Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: 
HUH?! SPEAK UP, GIRL!

unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) 
and yells back: 

NO, NOT SINCE 1938!

To make your program really believable, have Grandma shout a different year each time, 
maybe any year at random between 1930 and 1950. 
(This part is optional and would be much easier if you read the section on Python’s random number 
generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE. 


- Hint: Try to think about what parts of your program should happen over and over again. 
All of those should be in your while loop. 

- Hint: People often ask me, “How can I make random give me a number in a range not starting at zero?” 
But you don’t need it to. Is there something you could do to the number random returns to you? 

- Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, 
she could pretend not to hear you. Change your previous program so that you have to shout 
BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, 
you should still be talking to Grandma. 
'''

# from random import randint

# grandma = ""
# print("Grandma is so happy she can finally talk with somebody. \nHi, dear! How are you?")
# user = input()

# while user != "BYE" * 3:
# 	if user.islower():
# 		print("HUH?! SPEAK UP, GIRL!")
# 		user = input()
# 	elif user.isupper():
# 		print("NO, NOT SINCE " + str(randint(1930, 1950)))
# 		user = input()
# print("Bye to you too, honey!")






'''Leap years. Write a program that asks for a starting year and an ending year 
and then puts all the leap years between them (and including them, if they are also leap years). 
Leap years are years divisible by 4 (like 1984 and 2004). 
However, years divisible by 100 are not leap years (such as 1800 and 1900) unless 
they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess! '''

'''
firstYear = int(input())
secondYear = int(input())


for x in range(firstYear, secondYear + 1):
	if x % 400 == 0: 
		print(x)
	elif x % 4 == 0 and x % 100 != 0:
		print(x)
	'''


'''
A tree has 5842 leaves every year. In 200 years, how many leaves would've had 150 trees?
'''
'''
leaves = 5842
years = 200
trees = 150

print(leaves * years * trees)'''



''' Building and sorting an array. Write the program that asks us to type as many words as we want 
(one word per line, continuing until we just press Enter on an empty line) and then repeats the words
 back to us in alphabetical order. Make sure to test your program thoroughly; for example, 
 does hitting Enter on an empty line always exit your program? Even on the first line? And the second? 

Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it! '''

# userArray = []
# print("Your list: ")
# only_enter_pressed = False
# while not only_enter_pressed:
#     word = input('Enter word: ')
#     if not word:
#         only_enter_pressed = True
#     else:
#         userArray.append(word)

# print(sorted(userArray))


'''Table of contents. Write a table of contents program here. Start the program with a list 
holding all of the information for your table of contents (chapter names, page numbers, and so on). 
Then print out the information from the list in a beautifully formatted table of contents. 
Use string formatting such as left align, right align, center.'''

# babyBook = ("Baby-bit: ", "page 12", "while (food())", "page 62", "play(dad)", 
# 	"page 98", "mom = 'code_and_cola'", "page 133", "no_sleep == true", "page 250")
# print("-" * 40)
# print("\n " +  "Baby and code".center(40) + "\n")
# print("-" * 40 + "\n")
# width = 30
# i = 0
# while (i < len(babyBook)):
# 	print(babyBook[i].ljust(width), babyBook[i+1].ljust(width))
# 	i+=2


#Write a function that prints out "moo" n times.
# def print_moo(n):
# 	print("moo" * n)

# print_moo(5)

