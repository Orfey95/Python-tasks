def count(n):
    while n != 0:
        yield n - 1
        n -= 1


for i in count(5):
    print(i)
