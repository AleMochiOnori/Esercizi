def is_palindrome(x : int) -> bool :
    s: str = str(x)
    i : int = 0
    while i < len(s):
        j = len(s) - (i+1)
        if s[i] != s[j]:
            return False
        i += 1
    return True    

        

        
print(is_palindrome(121))        





from collections import Counter 
def lenght_of_last_word(s : str) -> int :
    l: list[str] = s.split()    # Usando lo split elimino gli spazi. Lo split ritorna una lista con ogni parola origanariamente separta da spazi come singolo elemento.
    return len(l[-1])

print(lenght_of_last_word("viva il falchetto"))









def convert_to_title(col_number: int ) -> str :
    result = ""
    while col_number > 0:
        resto = (col_number -1) %  26
        result = chr(resto + ord ('A')) + result
        col_number = (col_number - 1) // 26
        
    return result    


print(convert_to_title(34325235))    





def majority_element(nums: list[int]) -> int:
    lunghezza = len(nums) // 2
    for a in nums:
        if nums.count(a) > lunghezza :
            return a
        
    return None
        



print(majority_element([1,3,4,4,4,7,4,56,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,4,7]))



