"""
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# A simple example class
class Test:

    # A sample method
    def fun(self):
        print("Hello")


# Driver code
obj = Test()
obj.fun()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

p1.age = 40
p1.myfunc()
print(p1.age)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()
y = Student("Harry", "Potter")
y.printname()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("john", 22)

print(p1.name, p1.age)

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("Hello my name is " + self.name + "\n")
        print("and my age is " + str(self.age) + "\n")


p1 = Person("John", 21)
p2 = Person("Abc", 98)
p3 = Person("DFG", 66)

p1.myfunction()
p2.myfunction()
p3.myfunction()
