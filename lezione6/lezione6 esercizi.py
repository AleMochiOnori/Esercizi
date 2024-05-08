# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant :
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describeRestaurant(self):
        print(self.restaurant_name,self.cuisine_type)

    def openRestaurant(self) :
        print("The restaurant" , self.restaurant_name,"is open")

ristorante = Restaurant("Bottarolo","Cucina italiana")
ristorante.describeRestaurant()
ristorante.openRestaurant()


print()


# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.


ristorante1 = Restaurant("Haiku","Giapponese/Cinese")
ristorante2  = Restaurant("Burger King","Fast food")
ristorante1.describeRestaurant()
ristorante1.openRestaurant()
ristorante2.describeRestaurant()
ristorante2.openRestaurant()



print()





# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.



class User :
    def __init__(self, first_name : str , last_name : str , age : int , gender : str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.gender = gender

    def describe_user(self):
        print(f"Name : {self.first_name}, Lastname : {self.last_name}, Age : {self.age}, Gender : {self.gender}")


    def greetUser(self):
        print(f"Welcome back!!")

user1 = User("Lorenzo","De Medici", 700 , "Male")
user2 = User("Franco", "Arcieri" , 70 ,"Male")
user3 = User("Francesca","Caroselli", 25, "Female")

user1.describe_user()
user1.greetUser()
user2.describe_user()
user2.greetUser()
user3.describe_user()
user3.greetUser()


print()






# 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 


class Restaurant :
    def __init__(self,restaurant_name,cuisine_type,numberServed = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numberServed = numberServed

    def describeRestaurant(self):
        print(self.restaurant_name,self.cuisine_type,self.numberServed)

    def openRestaurant(self) :
        print("The restaurant" , self.restaurant_name,"is open")
    
    def set_number_served(self,number) :
        self.numberServed = number
        print(f"Clients served  during a causal day in a week  -- {self.numberServed}")

    def  increment_number_served(self) :
        for i in range(1,501,1) : #Putting only 50 people to not mess the terminal
            self.numberServed = i
        print(f"Clients served during weekend with Rush  -- {self.numberServed}")

restaurant = Restaurant("McDonald's","Fast Food", numberServed = 0)
restaurant.describeRestaurant()
restaurant.numberServed = 10
restaurant.describeRestaurant()
restaurant.set_number_served(100)
restaurant.increment_number_served()


print()



# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User :
    def __init__(self, first_name : str , last_name : str , age : int , gender : str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.logging_attempts = None

    def logging_attempts2(self) :
        print("Il numero di log è :" , self.logging_attempts)


    def increment_login_attempts(self,attempts):
        self.logging_attempts = attempts
        self.logging_attempts += 1

    def  reset_login_attempts(self):
       self.logging_attempts = 0


Roberta = User("Roberta","Falconieri", 25 , "Female") 
Roberta.increment_login_attempts(3)         
Roberta.logging_attempts2()
Roberta.reset_login_attempts()
Roberta.logging_attempts2()


print()



# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 




class IceCreamStand :
    def __init__(self,restaurant_name,cuisine_type, flavors) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors


    def display_flavors(self):
        print(self.flavors)





iceCream = IceCreamStand("The best ice cream","Ice Cream",["Chocolate", "Vanilla", "Strawberry"])

iceCream.display_flavors()


print()






# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 




class Admin :
    def __init__(self, first_name : str , last_name : str , age : int , gender : str, privileges : list):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.privileges = privileges

    def showPrivileges(self):
        for a in self.privileges :
            self.privileges = a
            print(self.privileges)        

admin = Admin("Carlo" , "Grappi" , 35 , "Male" , ["Can add post", "Can delete post " , "Can ban user"])        
admin.showPrivileges()

print()



# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.



class Admin2 :
    def __init__(self, first_name : str , last_name : str , age : int , gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.privileges = Privileges(["Can add post", "Can delete post " , "Can ban user"])
        
    def showPriviliges(self):
        self.privileges.showPrivileges()



class Privileges :
    def __init__(self,privileges):
        self.privileges = privileges
    def showPrivileges(self):
        for a in self.privileges :
            self.privileges = a
            print("Admin" , self.privileges)        



admin2 = Admin2("Flavio" , "Barzotti" , 3 , "Male",)

    
admin2.showPriviliges()   






# 9-9 