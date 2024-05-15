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
        self.health = round(100 * (1 / age), 3)




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
        if animal.animalArea <  fence.area  and animal.preffered_habitat ==  fence.habitat and fence.temperature > 20 and animal not in fence.animals:
            fence.animals.append(animal)


    def remove_animal(self , animal : Animal , fence : Fence ) :
        if fence.animals != [] :
            fence.animals.remove(animal)
            occupation = fence.area - animal.animalArea
            fence.area = occupation + animal.animalArea

    def feed(self , animal : Animal) :
        for animal in fence.animals :
            if animal in fence.animals :
                if animal.animalArea <= fence.area :
                    animal.animalArea = animal.animalArea * 1.02
                    animal.health = animal.health * 1.01             

    def clean(self, fence : Fence) :
        if fence.area == 0:
            return f"fence area is {residual}"
        for animal in fence.animals :  
            animalArea = animal.width * animal.height
            residual = fence.area - animalArea
            fence.area = residual + animalArea
            cleaningTime = residual / animalArea
        return cleaningTime   
        

    def describe_zoo(self):
        print()
        for zookeeper in zookeepers :
            print(f"- Guardians of the zoo  =   Name : {zookeeper.name} , Lastname : {zookeeper.lastName} , ID  : {zookeeper.id}" )
            print()
        for animal_fence in fences:
            print(f"- Fence Habitat : {animal_fence.habitat} , Temperature : {animal_fence.temperature}, Area is : {animal_fence.area}")  
        for animal in fence.animals:
            rounded = round(animal.health)
            print()
            rounded2 = round(animal.animalArea)
            print(f"- Animal Name : {animal.name} , Species : {animal.species} , Age : {animal.age} Height : {animal.height} , Width : {animal.width} , Preferred habitat : {animal.preffered_habitat}")
            print(f"- Area of {animal.name} is {rounded2}")
            print(f"- Health of {animal.name} is {rounded}")
        


#######################################################################


# Guardians :

custodeZoo = Zookeeper("Francesco" , "Adriani" , 234)
custodeZoo2 = Zookeeper("Flavio" , "Strati" , 30)

zookeepers : list = [custodeZoo,custodeZoo2]

# Fences :

fence = Fence(200 , 34 , "Savana")  # Istance of Fence class to initalize fence values
fence2 = Fence(600 , 45 , "Savana")  # Istance of Fence class to initalize fence values

fences = [fence,fence2]

# With Animals

leon = Animal("Bity" , "Leon", 6 , 10, 2 , "Savana")
zebra = Animal("Lines" , "Zebra", 20 , 5 , 10 , "Savana" )
elephant = Animal("Ruffo" , "Elephant" , 3 , 9 , 40 ,"Savana")



custodeZoo.add_animal(leon,fence)
custodeZoo.add_animal(elephant,fence)
custodeZoo.feed(leon)
custodeZoo.describe_zoo()





#####################################################################


