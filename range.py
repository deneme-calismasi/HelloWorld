a = list(range(4, 18, 2))
b = [*range(2, 16, 2)]
c = [0, 2, 4, 6, 8, 10, 12]

for n in range(0, 3, 1):
    for m in range(n, 6, 2):
        for o in range(n, m, 3):
            print(o)

for d in zip(a, b, c):
    print(d)


def get_number():
    print(5)


def get_count():
    return 5


def return_number(count):
    return count


def return_count(number=22):
    return number


print(get_number())
print(get_count())
print(return_count(33))
print(return_number(55))
