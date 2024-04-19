


def area(x:float,y:float) -> float :

    return x * y



x, y = (2,3)
out = (area(2,5))

print(out)




def substract(a : int , b :int) -> int:
    subtraction = a - b
    return subtraction


print(substract(10,5))





def sum(l: list [float]) -> float:

    somma = 0
    for el in l :
        somma += el
    return somma 

result = sum([2,5,4,5,6,4,6,9])

print(result)




def check_value(a:int , check : int) -> str:
    if a >= check :
       return "the number is bigger or equal than 5"
    else: 
       return "the number is smaller than 5"


print(check_value(5 , 6))        




def check_lenght(a:str) -> str :
    if len(a) > 10:
        return "string is bigger than 10 charachters"
    elif len(a) < 10 :
        return "string is smaller than 10 charachters"
    else :
        return "string is equal to 10 charachters"
    
print(check_lenght("Cikolino"))   


def print_number(a : list) -> int:
  
    for i in a :
        print(i)
print_number([2,6,5,5,7])   



def check_each(a : list) -> str:
    for i in a:
        if  i > 5 :
            print("the number is bigger than 5")
        elif i < 5 :
            print ("the number is smaller than 5")
        else :
            print("the number is equal to 5")     
check_each([2,6,4,5,9,4])

