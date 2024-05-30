def seconds_since_noon(ore : int , minuti : int , secondi : int) -> int : 
        oraInSecondi = 3600
        secondiInMinuto  = 60
        minuti = minuti * secondiInMinuto
        ore = ore * oraInSecondi
        secondiDalle12 =  minuti + ore + secondi
        return secondiDalle12
print(seconds_since_noon(0,0,0))    


def time_difference(ora1 , minuto1 , secondi1 , ora2 , minuto2 , secondi2):
        time1 =  seconds_since_noon(ora1 , minuto1 , secondi1)
        time2 =  seconds_since_noon(ora2 , minuto2, secondi2) 
        if time1 < time2 :
            time_difference1 = time2 - time1
            return time_difference1
        elif time1 == 0:
            mezzanotte = 0
            mezzanotte += time2
            return mezzanotte
        else:
           time_difference2 = time1 - time2
           return time_difference2
 
print(time_difference(23,59,59,1,2,3))