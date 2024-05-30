def seconds_since_midnight(ore: int, minuti: int, secondi: int) -> int:
    # Convertire ore, minuti e secondi in secondi
    ora_in_secondi = 3600
    secondi_in_minuto = 60
    minuti = minuti * secondi_in_minuto
    ore = ore * ora_in_secondi
    secondi_dalle_mezzanotte = minuti + ore + secondi
    return secondi_dalle_mezzanotte

def time_difference(ora1: int, minuto1: int, secondi1: int, ora2: int, minuto2: int, secondi2: int) -> int:
    # Calcolare i secondi dalla mezzanotte per entrambi gli orari
    time1 = seconds_since_midnight(ora1, minuto1, secondi1)
    time2 = seconds_since_midnight(ora2, minuto2, secondi2)
    
    # Calcolare la differenza assoluta in secondi
    time_difference_in_seconds = abs(time2 - time1)
    return time_difference_in_seconds

# Esempio di test
print(seconds_since_midnight(0, 0, 0))  # Output: 0

print(time_difference(0, 0, 0, 1, 2, 3))  # Output: 3723
