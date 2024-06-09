def fii1(a, b):
    n = []
    for v in a:
        if v in b:
            n.append(v)
    return n


def fii2(a, b):
    n = set()
    for v in a:
        if not v in b:
            n.add(v)
    n = list(n)
    return n


lst1 = [1, 8, 4, 5, 1, 0, 5, 3]
lst2 = [6, 2, 0, 1, 6, 5, 5, 9]
ts1 = fii1(lst1, lst2)
ts2 = fii2(lst1, lst2)
ts3 = fii2(lst2, lst1)
print(ts1)
print(ts2)
print(ts3)
