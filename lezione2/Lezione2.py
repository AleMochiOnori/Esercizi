#Alessandro mochi onori 18/04/2024

print("Hello world")


#Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”


#Esercizio 1

Eric: str = "Eric,"

ericMessage: str = 'would you like to learn some Python today?'


print("Hello " , Eric , ericMessage)


#Esercizio 2

#Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.


flavio:str = "Flavio"


print(flavio.lower(),flavio.upper(),flavio.title())

#Esercizio 3

#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following,
# including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

obiwan: str = "Obiwan said to general Gravious : "
phrase:str = "Hello there"


print(f"{obiwan}{phrase}")



#Esercizio 4


famous_person:str = "Bruce lee once said : "
phrase: str = "i don't fear someone who practised 100 combat moves but i fear someone who practised one 100 times"

message:str  = f"{famous_person}{phrase}"

print(message)



# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. 
# hen use the removesuffix() method to display the filename without the file extension, like some file browsers do.



file_name = 'python_notes.txt'


print(file_name.removesuffix('.txt'))



#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.


names: list = ['francesco','flavio','ideri']


print(names[0],names[1],names[-1])


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, 
# but each message should be personalized with the person’s name.


print(f"ti va di sucire oggi {names[0]}, ti va di uscire oggi {names[1]},ti va di uscire oggi {names[2]}")


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


carList:list = ['2006 used Toyota Yaris','Lamborghini','Ferrari']

print(f'i would like to own a {carList[1]} and a {carList[2]} but i have mere {carList[0]} ')


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
#T hen use your list to print a message to each person, inviting them to dinner.



livingAndDead: list = ['Hitler' , 'Ghandi' , 'Robertino', 'Elon Musk']


message: str = f"hey {livingAndDead[0]} would you like to come for a dinner? there will be {livingAndDead[1]} too , he admires you for what you have done. {livingAndDead[2]} will come with {livingAndDead[3]}. {livingAndDead[2]} will probably say to {livingAndDead[-1]} , ' hai trovato un bel lavoretto' "


print(message)


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

livingAndDead[2] = "Mussolini"

message1:str = f"Hi {livingAndDead[0]} would you come for a dinner tonight ?  "
message2:str = f"Hi {livingAndDead[1]} would you come for a dinner tonight? "
message3: str = f"Hi {livingAndDead[2]} would you come for a dinner tonight?"
message4: str = f"Hi {livingAndDead[3]} would you come for a dinner tonight?"
print(message1,message2,message3,message4)


print(livingAndDead[2], "won't come to the dinner")
