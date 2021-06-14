def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 3
print(factorial(num))


def set_list(list):
    list = ["A", "B", "C"]
    return list


def add(list):
    list.insert(0, "D")
    return list


lst = []

try:
    n = int(input("Enter number of elements : "))
except ValueError:
    print("Please enter only a integer")
for i in range(0, n):
    ele = str(input())

    lst.append(ele)

print(set_list(lst))

print(add(lst))
