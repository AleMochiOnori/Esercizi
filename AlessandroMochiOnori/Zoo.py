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
        self.animalArea = height * width
        self.health = 10




class Fence :
    def __init__(self,area, temperature, habitat) :
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []



class Zookeeper :
    def __init__(self,name,lastName,id):
        self.name = name
        self.lastName = lastName
        self.id = id


    def add_animal(self, animal : Animal , fence  : Fence) :
        if animal.animalArea  <  fence.area and animal.preffered_habitat == "Savana" and fence.habitat == "Savana" and fence.temperature > 20 and animal not in fence.animals:
            fence.animals.append(animal)
            occupation = fence.area - animal.animalArea
            print(f"added {animal.name} occupied {occupation}")
        else : 
            print(f"{animal.name} is too big or it's not his habitat")    

    def remove_animal(self , animal : Animal , fence : Fence ) :
        if fence.animals != [] :
            fence.animals.remove(animal)
            occupation = fence.area - animal.animalArea
            fence.area = occupation + animal.animalArea
            rounded = round(fence.area)
            print(animal.name , "has been removed and fence area is reset to", rounded)
        else :
            print(animal.name , "is not in the fence")

    def feed(self , animal : Animal) :
        residual = fence.area - animal.animalArea
        fence.area = residual + animal.animalArea
        if animal.animalArea <= fence.area and animal in fence.animals:
            animal.health = animal.health * 1.01
            rounded = round(animal.health)
            if animal.health >= 100 :
                print(f"{animal.name} cannot be fed again. He's too healty")
            animal.animalArea = animal.animalArea * 1.02
            rounded2 = round(animal.animalArea)
            print(f"{animal.name} health is {rounded} and his area is {rounded2}")    
        else :
            print(f"{animal.name} cannot be fed")


    def clean(self, fence : Fence) -> float :
        if fence.area == 0:
            return f"fence area is {fence.area}"
          



#######################################################################


# Guardians :

custodeZoo = Zookeeper("Francesco" , "Adriani" , 234)

# Fences :

fence = Fence(200 , 34 , "Savana")  # Istance of Fence class to initalize fence values

# With Animals

leon = Animal("Bity" , "Leon", 6 , 10, 2 , "Savana")
zebra = Animal("Lines" , "Zebra", 20 , 5 , 10 , "Savana" )
elephant = Animal("Ruffo" , "Elephant" , 3 , 3 , 40 ,"Savana")



#####################################################################