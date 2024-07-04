def generatore():
    yield "A"
    yield "B"
    yield "C"

provaGeneratore = generatore()



print(next(provaGeneratore))
print(next(provaGeneratore))



from contextlib import contextmanager 


@contextmanager

def context(*args):
    import time 


    start_time  :float  = time.time()


    yield


    end_time:float = time.time()
    elapsed_time:float = end_time - start_time


    print(f"{elapsed_time=}")

import sys

lista = []


a = lista

print(sys.getrefcount(a))

import time

def trhead_func(name):
    print(f"{name} Time - {time.time()}")
    time.sleep(2)
    print(f"{name} Time - {time.time()}")



import threading
for i in range(3):
    x = threading.Thread(target=trhead_func , args=(1,) )
    print("Prima di Thread")
    lista.append(x)
    x.start()

print("Thread partito")

print("Thread finito???")

def funzione(id: int):
    import time
    import random
    
    sleep_time: int = random.randint(1, 10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")
    
if __name__ == "__main__":
    
    import threading
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(100))
   