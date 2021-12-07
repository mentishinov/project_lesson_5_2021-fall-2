import time
from collections import OrderedDict
from functools import lru_cache

def cache(size=3):
    def decorator_cache(fn):
        cache_dict = OrderedDict()
        def wrapper(*args):
            if args not in cache_dict:
                if len(cache_dict) == size:
                    cache_dict.popitem(last=False)
                result = fn(*args)
                cache_dict[args] = result
            return cache_dict[args]
        return wrapper
    return decorator_cache

@lru_cache(maxsize=3)
def my_sleep():  # @decorator_cache -> my_sleep = decorator_cache(my_sleep)
    time.sleep(3)

if __name__=='__main__':
    t0 = time.time()

    my_sleep()

    print(time.time() - t0)

    print(my_sleep.cache)