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




# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.




livingAndDead.insert(0,"Goku")
livingAndDead.insert(3,"Vegeta")
livingAndDead.append("Gravelord Nito")
print(livingAndDead)




# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


print("unfortunately only two people may enter my door.")

livingAndDead.pop(0)
print(f"Goku i can't invite you to the dinner")
print(livingAndDead)
livingAndDead.pop(0)
print(livingAndDead)
print("Hitler i can't invite you to the dinner")
livingAndDead.pop(0)
print("Ghandi i can't invite you to the dinner")
print(livingAndDead)
livingAndDead.pop(0)
print("Vegeta i can't invite you to the dinner")
print(livingAndDead)
livingAndDead.pop(0)
print("Mussolini i can't invite you to the dinner")


print(livingAndDead)
print(f"congratulation {livingAndDead[0]} you made it!! , and you {livingAndDead[-1]} as well!!")


del livingAndDead[0]
del livingAndDead[0]

print(livingAndDead)







# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.





locations: list = ["Cuba" , "New York" , "Spain" , "China" , "Antartic"]

print(locations)




ordered: list = sorted(locations)

print(locations)




reversed : list = sorted(locations, reverse = True)

print(locations)





locations.reverse()

print(locations)




locations.sort()

print(locations)


locations.sort(reverse=True)
print(locations)


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.


print("people invited are" , len(livingAndDead))




# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

listaConTanteCose : list = ["Rome","San Franscisco","Belen Rodriguez"]

listaConTanteCose.insert(0,"Mount White")
listaConTanteCose.append("Amsterdam")
listaConTanteCose.pop(0)
listaConTanteCose[1] = "Bello de casa"
del listaConTanteCose[3]
listaConTanteCose.sort()
x = sorted(listaConTanteCose)
listaConTanteCose.reverse()





# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.



person : dict = {
    "name" : "Osama",
    "Last name" : "Rossi",
    "Age" : 22,
    "City" : "Reggio Calabria"
}

print(person["name"],person["Last name"],person["Age"],person["City"])




# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.



favouite_Numbers : dict = {
    "Alessio" : 2,
    "Flavio": 20,
    "Alessandro" : 3,
    "Roberta" : 50,
    "Cikolino" : 10
}



print("Il numero preferito di Alessandro è :", favouite_Numbers["Alessandro"],
      "Il numero preferito di Flavio è :", favouite_Numbers["Flavio"],  
      "Il numero preferito di Cikolino è :", favouite_Numbers["Cikolino"],
      "Il numero preferito di Robrta è :", favouite_Numbers["Roberta"],
      "Il numero preferito di Alessio è :", favouite_Numbers["Alessio"]
      )




# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.






glossary = {
    "Variable": "A name associated with a value stored in the computer's memory.",
    "Function": "A reusable block of code that performs a specific action.",
    "Loop": "A control structure that repeats a block of instructions as long as a condition is true.",
    "List": "An ordered and modifiable collection of elements.",
    "Method": "A function associated with an object that operates on it."
}




for a,b in glossary.items() :    # For loop with 2 variables, function .items() to access the glossary.
    print(f"{a} :")
    print(f"{b}\n")



# 6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.




people : list = [
    {
        "Alessio" : 2,
        "Flavio": 20,
        "Alessandro" : 3,
        "Roberta" : 50,
        "Robertino" : 10
    
    },


    {
        "Manuel" : 10,
        "Lucas" : "ciao",
        "Martina" : "i like pizza",
        "Electra" : "i drive very fast!!",
        "Elon" : "I produce teslas"
        
    },
    {
        "Mario": "I jump on people",
        "Federica": "I really like to swim",
        "Shumaker": "I'm a pro driver with F1",
        "Jonny Depp": "I really loved to perform for all my films especially Pirate of Carribean",
        "Brad Pitt": "ETTTOOOREEEEE !!!!!",
    }
]



for dizionario in people:
    for a, b in dizionario.items():
        print(f"{a}: {b}")
    print()  # Aggiunge una riga vuota tra ogni dizionario


# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet. 




pets = [
    {
        "Alessio": "cat",
        "Flavio": "Iguana",
        "Alessandro": "Snake",
        "Roberta": "Dog",
        "Robertino": "Bird"
    },
    {
        "Manuel": "Horse",
        "Lucas": "Cow",
        "Martina": "Duck",
        "Electra": "Pig",
        "Elon": "Goat"
    },
    {
        "Mario": "Bunny",
        "Federica": "Lion",
        "Shumaker": "Tiger",
        "Jonny Depp": "Elephant",
        "Brad Pitt": "Zebra",
    }
]

for dictionary in pets:
    for a, b in dictionary.items():
        print(f"{a}: {b}")
    print()




# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.




favorite_places = {
    "Alice": ["Paris", "Kyoto", "New York"],
    "Bob": ["Rome", "Sydney","Dubai"],
    "Charlie": ["London","Moscow","Alabama"]
}

for a, b in favorite_places.items():
    print(f"{a}'s favorite places are:")
    for place in b:
        print(f"{place}")
    print() 





# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.



numbers_people : list = [
    {
        "Alessio" : [2,30],
        "Flavio": [2,40],
        "Alessandro" : [3,4],
        "Roberta" : [3,5],
        "Robertino" : [50,43]
    
    },


    {
        "Manuel" : [20,34,32],
        "Lucas" : [10,31],
        "Martina" : [90,67,54],
        "Electra" : [23,67,98],
        "Elon" : [34,65,34]
        
    },
    {
        "Mario": [45,45,334],
        "Federica": [34,32,4,6],
        "Shumaker": [45,3,5,7],
        "Jonny Depp": [4,5,76,4],
        "Brad Pitt": [2,5,3,6],
    }
]




for dictionary in numbers_people:
    for a, b in dictionary.items():
        print(f"The favourite number of {a} is")
        for x in b:
            print(f"- {x}")     
        print()

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.



cities = {
    "Rome": {
        "Country": "Italy",
        "Population": "3 million",
        "Fun fact": "Every year a man dives into the Tiber River"
    },
    "New York": {
        "Country": "USA",
        "Population": "Six million",
        "Fun fact": "Every alien ship in movies somehow lands in this city"
    },
    "Amsterdam": {
        "Country": "Netherlands",
        "Population": "821 thousand",
        "Fun fact": "Amsterdam is known for its creative and recreational atmosphere"
    }
}



for city, info in cities.items():
    print("--", city)
    print()
    for key, value in info.items():
        print(f"{key}: {value}")
    print()


#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.    



complex = [
    {
        "Alessio": [2, 30, {"ciao"}],
        "Flavio": [2, 40, {"ciao"}],
        "Alessandro": [3, 4, {"ciao"}],
        "Roberta": [3, 5, {"ciao"}],
        "Robertino": [50, 43, {"ciao"}]
    },
    {
        "Manuel": [20, 34, 32, {"ciao"}],
        "Lucas": [10, 31, {"ciao"}],
        "Martina": [90, 67, 54, {"ciao"}],
        "Electra": [23, 67, 98, {"ciao"}],
        "Elon": [34, 65, 34, {"ciao"}]
    },
    {
        "Mario": [45, 45, 334, {"ciao"}],
        "Federica": [34, 32, 4, 6, {"ciao"}],
        "Shumaker": [45, 3, 5, 7, {"ciao"}],
        "Jonny Depp": [4, 5, 76, 4, {"ciao"}],
        "Brad Pitt": [2, 5, 3, 6, {"ciao"}]
    }
]


for dictionary in complex:
    for a,b in dictionary.items():
        print(a,b)
        for x in b[-1]:
            print(x)
            print()    