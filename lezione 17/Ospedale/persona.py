class Persona:
    def __init__(self,first_name,last_name):
        if type(first_name) == str and type(last_name) == str:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__età = 0
        else:
            print("il nome non è una stringa")
            self.__età = None
            self.__first_name = None
            self.__last_name = None



    def setName(self,first_name):
        if type(first_name) == str:
            self.__first_name = first_name
        else :
            print("Il nome inserito non è una stringa")


    def setLastName(self,last_name):
        if type(last_name) == str :
           self.__last_name = last_name
        else :
            print("Il cognome non è una stringa")     


    def setAge(self,age):
        if type(age) == int :
            self.__età = age
            return self.__età
        
    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    

    def getAge(self):
        return self.__età
    
    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__età} anni")



