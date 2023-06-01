import functools
import tracemalloc


def memory_usage(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')[:10]
        print("Memory usage:")
        for stat in top_stats:
            print(stat)
        tracemalloc.stop()
        return result

    return deco


@memory_usage
def test_func(lst_len):
    """
        The function takes a number(lst_len)
        and returns a list of numbers from 0 to number(lst_len)
    """
    lst = [x for x in range(lst_len)]
    return lst


test_func(1000)