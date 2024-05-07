if False:
    def visit_tree(tree : dict[int,list],n: int) :
        left_child,right_child = tree[n]
        if left_child :
            visit_tree(tree,left_child)
        if right_child:
            visit_tree(tree,right_child)


tree : dict = {1:[2,3],2:[4,5],3 :{None,None},4 : {None,None},5 :{None,None}}   
#visit_tree(tree,1)     


def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    result = {}
    stack: list[int] = [root]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            left_child, right_child =\
                tree[curr_node]
            if left_child: 
                stack.append(left_child)
            if right_child:
                stack.append(right_child)
    return result            




class Person :
    def __init__(self, name:str, username:str , age:int):
        self.name = name
        self.username = username
        self.age = age

 


    def add_hobby(self,hobby) :
        self.hobbies.append(hobby)  

    def __str__(self) -> str:
        return f"asdawd"

swarmer = Person("Valerio","Montieri",25)    
snappiest6 = Person("Flavio","Pesci",24)
print(swarmer,snappiest6)    



if swarmer.age > snappiest6.age :
    print(swarmer.name)
lista = [
    Person("Francesco","Rossi", 5),
    Person("Romiro","Togliatti", 55),
    Person("Giacomino","Franchi", 33),
    Person("Valerio","Increduli", 78),
    Person("Fabio","Nutelli", 10)
]    




min_age = float("inf")  # Initializing a variable that is the maximum possible
index_min_age = 0

for i, persona in enumerate(lista):
    if persona.age < min_age:
        min_age = persona.age
        index_min_age = i
print(index_min_age)


class Student :
    def __init__(self, name, studyprogram):
        self.name = name
        self.studyprogram = studyprogram
        self.gender = None
        self.age = None


    def set_age(self , age):
        self.age = age

    def set_gender(self,gender):
        self.gender = gender


    def __str__(self) -> str:
      return  f"Nome :{self.name}, Studies : {self.studyprogram} Age {self.age}"   

Niccolò = Student("Niccolo","FullStack")
Alessandro = Student("Alessnadro","Fullstack")
Emanuele = Student("Emanuele","Fullstack")        






Niccolò.set_age(10)
print(Niccolò)





class Animal:
    def __init__(self,animal,legs = 0):
        self.animal = animal
        self.legs = legs
    def getLegs(self,legs):
      return self.legs
    def setLegs(self,leg):
        if leg >= 0:
            self.leg = leg
    def __str__(self) -> str:
      return  f"l'animale è : {self.animal} e le sue gambe sono {self.legs}"    

Toro = Animal("Toro",4)
Ragno = Animal("Ragno",8)

Toro.legs = 6

print(Toro)



class Food:
    def __init__(self,name,price,description) -> None:
        self.name = name 
        self.price = price 
        self.description = description

    def __str__(self) -> str:
        return f'Food(name={self.name}, price={self.price}, descr={self.description})'

class Menu :
    def __init__(self,food = []) :
        self.food: list[Food] = food

    def addFood(self, food: Food):
        self.food.append(food)

    def removeFood(self, food: Food):
        self.food.remove(food)   


    def __str__(self) -> str:
        s = ""
        for food in self.food:
            s += "; " + food.__str__()
        return s




cibi = [
         Food("Carbonara",10,"Pasta con uovo, pecorino ,  guanciale"),
         Food("Cacio e pepe",8,"Pasta con cacio e pepe"),
         Food("Vongola",10,"Cibo tipico marino italiano")
        ]

menu = Menu(food=cibi)  
print(menu)