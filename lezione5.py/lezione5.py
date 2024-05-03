# Esercizio 1

def sum_above_threshold(numbers: list[int],Threshold) -> int:
    sum = 0
    for num in numbers:
        if num > Threshold:
            sum = sum + num
    return sum

print(sum_above_threshold([1, 10, 20, 30], 10))


# Esercizio 2



def countdown(n: int) -> int:
    for a in range(n,-1,-1):
        print(a)
    

print(countdown(5))




# Esercizio 3 





def find_element(lst: list[int], element: int) -> bool:
        if element in lst :
            return True 
        else :
            return False
        

print(find_element([2,3,4,5],2))






def rounded_average(numbers: list[int]) -> int:
    count = 0
    sum = 0
    for x in numbers :
        count += 1
        sum = sum + x
    media = sum / count 
    rounded = round(media)
    return rounded  

print(rounded_average([1,4,6,4,4,7]))



def count_isolated(lista : list[int]) -> int:
   for a in lista :
       if a + 1 == a :
        return a
print(count_isolated([4,6,8,8,5,5,6,6]))






def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    return original_set - set(elements_to_remove)
print(remove_elements({2,3,5,7},{2,3}))




def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
  a =  {k:dict1.get(k, 0) + dict2.get(k, 0) for k in dict1.keys() | dict2.keys()}
  return a
print(merge_dictionaries({"Gelato" : "Cono" ,"Gusto" : "Cioccolato"},{"Gelato":"Coppa" , "Gusto" : "Crema"}))