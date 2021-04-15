"""i = 1
while i < 6:
    print(i)
    i += 1

x = 1
while x < 5:
    if x == 3:
        break
    i += 1

"""

a = 0
while a < 26:
    a += 2
    if a == 6 or a == 16:
        continue
    elif a == 22:
        break
    print(a)
