class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        if self.age < 25:
            print(self.name, "is younger than me")
        elif self.age == 25:
            print(self.name, "is the same age as me")
        elif self.age > 25:
            print(self.name, "is older than me")


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 25)

Person.compare_age(p1)
Person.compare_age(p2)
Person.compare_age(p3)
