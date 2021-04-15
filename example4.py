class Fruit:
    def __init__(self, weight, name="none"):
        self.name = name
        self.weight = weight

    def __add__(self, x):
        if isinstance(x, Fruit):
            return Fruit(self.weight + x.weight)
        if isinstance(x, int):
            return Fruit(self.weight + x, self.name)

    def __eq__(self, x):
        # Comparing names and not weights:
        if self.name == x.name:
            print("Both are the same fruits")
        else:
            print(self.name, "and", x.name, "are different fruits.")

    # Overloading __str__() to use print(Fruit):
    def __str__(self):
        if self.name == "none":
            return "Weight: {0}\n".format(self.weight)
        else:
            return "Name: {0}, Weight: {1}\n".format(self.name, self.weight)


a = Fruit(5, "Strawberry")
b = Fruit(100, "Watermelon")
c = Fruit(20, "Mango")

print(a, b, c)
print(a + b + c)
