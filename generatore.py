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

