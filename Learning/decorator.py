from _datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper()


@timeit
def one():
    l = [x for x in range(1000) if x % 2 == 0]
    return l


@timeit
def two():
    l = []
    for i in range(1000):
        if i % 2 == 0:
            l.append(i)
    return l


l1 = one()
l2 = two()

print(l1)
print(l2)
