import random

def mossaTartaruga():
    mossaTartaruga  = random.randint(1,10)
    posizione = 0
    if mossaTartaruga  >= 1 and mossaTartaruga  <= 5 :
        posizione = posizione + 3
    elif mossaTartaruga  >= 6 and  mossaTartaruga  <=  7:
        posizione = posizione - 6
        if posizione < 1 :
          posizione  = 0   
    elif mossaTartaruga  >= 8 and mossaTartaruga  <= 10:
        posizione += 1
    return posizione


def mossaLepre():
    mossaLepre = random.randint(1,10)
    posizione = 0      
    if mossaLepre >= 4 and mossaLepre <= 6 :
        posizione += 0
    elif mossaLepre >= 5 and mossaLepre <= 7:
        posizione += 9
    elif mossaLepre >= 8 and mossaLepre <= 9 :
        posizione += 12
    elif mossaLepre >= 1 and mossaLepre <= 3:
        posizione += 1
    elif mossaLepre >= 3 and mossaLepre <= 5 :
        posizione -= 2
        if posizione < 1 :
            posizione = 0        
    return posizione

def posizione():
    i = 0
    lista = ["_"] * 70
    while len(lista) < 70 :
        posizione_lepre = mossaLepre()
        posizione_tartaruga = mossaTartaruga()
        lista[posizione_lepre] = "T"
        lista[posizione_tartaruga] = "H"
        i += 1
        return posizione_lepre
print(posizione())

def Gara():
    if mossaLepre() == mossaTartaruga() :
     return "OUCH"
    if mossaLepre() == 70 :
        return "HARE WINS || YUCH!!!"
    if mossaTartaruga() == 70 :
        return "TORTOISE WINS! || VAY!!!"    
    if "T" == 70 and "H" == 70 :
        return "IT'S A TIE!!"
print(Gara())


