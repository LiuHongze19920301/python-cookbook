def func(n):
    yield n * 2


g = func(5)
for i in g:
    print(i)


def fib(n):
    pre, cur = 0, 1
    while n > 0:
        n -= 1
        yield cur
        pre, cur = cur, pre + cur


print([i for i in fib(10)])

gen = (x * x for x in range(10))
for i in gen:
    print(i)


def triangles(row=10):
    limit = 1
    L1 = [1]
    yield (L1)
    if row == 1:
        return
    limit += 1
    L2 = [1, 1]
    yield (L2)
    limit += 1
    while 1:
        if limit > row:
            break
        i = 0
        L3 = [1]
        while i < len(L2) - 1:
            L3.append(L2[i] + L2[i + 1])
            i = i + 1
        L3.append(1)
        yield (L3)
        limit += 1
        L1, L2 = L2, L3


for i in triangles(1):
    print(i)
