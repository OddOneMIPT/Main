def my_range(start, finish = None, step = 1):
    if finish is None:
        start, finish = 0, start
    current = start
    while current + step <= finish:
        yield current
        current += step

A = my_range(2, 7)


for i in A:
    print(i)

#Встроенные генераторы python
"""
range
map
enummmerate:
    работает так def enumer(X):
        i = 0
        for x in X:
            yield i,x
            i += 1

zip: работает так

"""
