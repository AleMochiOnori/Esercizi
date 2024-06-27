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