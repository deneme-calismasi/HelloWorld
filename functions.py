"""

def my_function(fname):
    print(fname + " Refsnes ")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


################

def my_function(*kids):
    print("The youngest child is " + kids[0])


my_function("Emil", "Tobias", "Linus")


################

def my_function(child3, child2, child1):
    print("The youngest child is " + child2)


my_function(child1="Emil", child2="Tobias", child3="Linus")


################

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


################

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


################

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

################

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)


# Driven code
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter Third number: "))
print("Maximum Number is: ", maximum(x, y, z))

################

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


################

mylist = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    mylist.append(numbers)


def multiplication(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result


print(multiplication(mylist))

"""


################

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
