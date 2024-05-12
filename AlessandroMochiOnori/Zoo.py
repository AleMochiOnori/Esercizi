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
        self.health = 0
        self.animalArea = height * width




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
        self.food = ["food"]


    def add_animal(self, animal : Animal , fence  : Fence = []) :
        if animal.animalArea  <  fence.area and animal.preffered_habitat == "Savana" and fence.habitat == "Savana" and fence.temperature > 20:
            fence.animals.append(animal)
            occupation = fence.area - animal.animalArea
            print(f"added {animal.name} occupied {occupation}")
        else : 
            print(f"{animal.name} is too big or it's not his habitat")    

    def removeAnimal(self , animal : Animal , fence : Fence  = []) :
        if fence.animals != [] :
            fence.animals.remove(animal)
            occupation = fence.area - animal.animalArea
            fence.area = occupation + animal.animalArea
            print(animal.name , "has been removed and fence area is reset to", fence.area)
        else :
            print(animal.name , "is not in the fence")

    def feedAnimal(self , animal : Animal) :
        occupation = fence.area - animal.animalArea
        fence.area = occupation + animal.animalArea
        if animal.animalArea < fence.area :
            animal.health = animal.health + 1
            animal.animalArea = animal.animalArea + 2
            print(f"animal health is {animal.health} and his area is {animal.animalArea}")    
        else :
            print(f"{animal.name} cannot be fed. He's too fat")









#######################################################################







# Francesco Adriani Zookeeper
# Savana Fence
# Animals : Leon , zebra , elephant

fence = Fence(500 , 34 , "Savana")  # Istance of Fence class to initalize fence values


leon = Animal("Bity" , "Leon", 6 , 10, 2 , "Savana")
zebra = Animal("Lines" , "Zebra", 20 , 5 , 10 , "Savana" )
elephant = Animal("Ruffo" , "Elephant" , 3 , 30 , 40 ,"Savana")


custodeZoo = Zookeeper("Francesco" , "Adriani" , 234)
custodeZoo.add_animal(leon,fence)
custodeZoo.removeAnimal(leon,fence)
custodeZoo.add_animal(zebra,fence)
custodeZoo.removeAnimal(zebra,fence)
custodeZoo.add_animal(elephant,fence)






#####################################################################