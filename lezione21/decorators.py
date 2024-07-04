# Esercizio 1 - Crea un decorator  che stampa n volte l'output della funzione decorata chiamandola due volte.




def decorator(num):
    def wrapper():
        print(num)
    return wrapper


def stampa():
    print(2)

ciao = decorator(stampa)
print(ciao)