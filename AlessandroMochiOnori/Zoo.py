class Zoo :
    def __init__(self,fences :str,zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers



class Animal:
    def __init__(self,name : str, species : str, age : int , height : float, width : float, preferred_habitat : str):
        self.name = name
        self.species = species 
        self.age = age
        self.height = height 
        self.width = width
        self.preffered_habitat = preferred_habitat
        self.health = None
        self.animalArea = height * width




class Fence :
    def __init__(self,animal,area, temperature, habitat) :
        self.animal = animal
        self.area = area
        self.temperature = temperature
        self.habitat = habitat



class Zookeeper :
    def __init__(self,name,lastName,id):
        self.name = name
        self.lastName = lastName
        self.id = id


    def add_animal(self, animal : Animal , fence  : Fence) :
        if animal.animalArea  <  fence.area:
            pass




crocodile = Animal("Bity","Cocodrile", 6 , 50 , 400 , "rivers")
fence = Fence(50 , 20 , "river")
