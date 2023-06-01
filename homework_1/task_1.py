import time
import functools
from collections import OrderedDict, defaultdict
import requests


def profile(msg="Elapsed time for function"):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            deco._num_call += 1
            result = f(*args, **kwargs)
            deco._num_call -= 1

            if deco._num_call == 0:
                print(msg, f'{f.__name__}: {time.time() - start}s')
            return result

        deco._num_call = 0
        return deco

    return internal


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in deco._cache:
                # Update the frequency count for the cache key
                deco._frequency[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                # Find the least frequently used cache key(s)
                min_freq = min(deco._frequency.values())
                min_freq_keys = [k for k, v in deco._frequency.items() if v == min_freq]
                # Remove the least frequently used cache key(s)
                del deco._cache[min_freq_keys[0]]
                del deco._frequency[min_freq_keys[0]]

            deco._cache[cache_key] = result
            deco._frequency[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        deco._frequency = defaultdict(int)
        return deco

    return internal


@profile(msg='Elapsed time')
@cache
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://google.com'))
print(fetch_url('https://google.com'))
print(fetch_url('https://google.com'))
print(fetch_url('https://ithillel.ua'))
print(fetch_url('https://dou.ua'))
print(fetch_url('https://ain.ua'))