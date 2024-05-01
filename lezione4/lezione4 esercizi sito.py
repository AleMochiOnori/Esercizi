# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

print()
def display_message() -> str :
    print("i'm learning python")



display_message()



print()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.



def favorite_book(title: str) -> str :
    print(title,"One of my favorite books is Alice in Wonderland")
favorite_book(title = "Alice in wonderland ---")


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(a: str , b: str) -> str :
        return a , b
print()
    
        
print(make_shirt("Size L","JUST DO IT"))
print(make_shirt(a =  "Size L", b = "JUST DO IT"))

print()
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size = 'Large', message = 'I love Python'):
    
    print(f"Size: {size}  Message: {message}")
  

make_shirt()

make_shirt(size = "Medium", message = "Python is for beginners" )


make_shirt(size = "Small" , message = "Python is lovely")
print()



# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.


def describe_city(city = "Reykjavik" , country = "Iceland") : 
    print(f"{city} is in {country}")

describe_city()
describe_city(city = "Rome" , country = "Italy")
describe_city(city = "New York" , country = "New York")
describe_city(city = "Berlin" , country = "Germany")
print()




# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.




def city_country(a : str , b: str) -> str :
    return a + b


print(city_country("Rome,", "Italy"))
print(city_country("Moscow,", "Russia"))
print(city_country("London,", "United Kingdom"))
print()



# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.


def make_album(artist , album, songsNumber = None ) -> dict:
    album = {"Artist ": artist, "Album" : album}
    if songsNumber:
        album['songs'] = songsNumber
    return album

print(make_album("Linkin Park" , "Meteora" , songsNumber= "13"))
print(make_album("If i were you", "InnerSignals"))
print(make_album("If i were you", "The Sleepless"))
print()


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.



if False : # Using if False for using the terminal without inserting the values every time. Remove it to try the program !!
        def make_album(artist , album, songsNumber = None ) -> dict:
            album = {"Artist ": artist, "Album" : album}
            return album
        while True : # Using True to be certain that the we can enter the loop and executing code without limitations; if not for the word break that stops the while loop.
            x = input("Enter The artist name :") # Using input() to store data about the artist name by the user. 
            f = input("Enter the album name :") # Using input() to store data about the artist name by the user.
            print(make_album(x,f))
            break
print()



# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.


def show_message(lista : list[str]) -> str :
    for a in lista :
        print(a)
messages : list[str] = ["Hey how are you", "You are late again!!!"]        

show_message(messages)

print()

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.



sent_messages =  []

def send_messages(messages,sent_messages) :
    for a in messages :
        print(a)
        sent_messages.append(a)
send_messages(messages , sent_messages)
show_message(messages)     
print()


# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.


messages_copy = messages.copy()
send_messages(messages,messages_copy)


print()

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def make_sandwich(*items):
    print("Ingredients :")
    for item in items:
        print("- " + item)


make_sandwich("Lettuce", "Tomato", "Mayo")
make_sandwich("Ham", "Cheese")
make_sandwich("Peanut Butter", "Jelly")


print()

# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"


def build_profile(firstName : str, lastName : str, age : int, weight : int, hairColor : str):
    profile = f"-{firstName} {lastName} , Age : {age}, weight : {weight} kg, Hair : {hairColor} "
    return profile
print(build_profile("Alessandro","Mochi onori", 25 , 75 , "Black" ))

print()

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 


def cars(maniafacture,model,color,tow_package = None):
    cars = {"Manufacturer": maniafacture,"Model": model,"Color": color}
    print(cars)
    return cars
cars( "Ford","Mustang","Red")
cars("Toyota","Pririus","Bue",tow_package=True)
print()




# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.



















# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import function
from function import add
from function import add as fn
import function as mn
from function import *
fn(add(2,6))
mn(add(2,3))
add(2,3)
print()
ciao = 2,9
ciao.__add__()
print(ciao)