class Number:
    def __init__(self, left, right):
        self.left = left
        self.right = right


number = Number(3, 2)

print("3+2=", number.left + number.right)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myFunc()
