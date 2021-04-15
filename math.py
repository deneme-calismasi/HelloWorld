import math


def function(x, y):
    a = pow(x, y)
    print(a)

    if x and y < 0:
        b = abs(x, y)
        print(b)
    else:
        pass

    c = min(x, y)
    d = max(x, y)
    print("Min:", c, "Max:", d)

    e = math.sqrt(x)
    f = math.sqrt(y)
    print(e)
    print(f)

    if x == float(x) and y == float(y):
        g = math.ceil(x)
        h = math.floor(y)
        print(g, h)
    else:
        pass


function(4.1, 8.8)
