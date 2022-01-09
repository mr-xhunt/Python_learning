# FUNCTION CACHING

import time
from functools import lru_cache

@lru_cache(maxsize=3) #we store latest 3 values  maxsize is how many no. of values you wish to store in cache but alert here it will be saved into ram dont write huge no
def some_work(n):
    #Some task which takes n seconds to run
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3) #only here the function takes its time and then it is saved into the cache memory 
    #and when the user again calls the fuction which is saved it will directly give result without any need to again run the function
    print("done!")
    some_work(3)
    print("Called again")
    some_work(3)
    print("Called again again...")
    some_work(3)
    print("Called again again...")
    some_work(3)
    print("Called again again...")
    some_work(3)
    print("Called again again...")
    some_work(3)
    print("Called again again...")
    some_work(3)
    print("Called again again...")
    
