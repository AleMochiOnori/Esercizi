import random



lista = ["_"] * 70
tempo = 0




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


def mossaLepre(posizione):
    mossaLepre = random.randint(1,10)  
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





def Gara():
    while True:
        lepre = mossaLepre(lepre)
        tartaruga = mossaTartaruga(tartaruga)
        lista[lepre] = "T"
        lista[tartaruga] = "H"


print(Gara())


