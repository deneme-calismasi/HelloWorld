from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(pi * self.radius ** 2)  # round because of error in test

    def get_perimeter(self):
        return round(2 * pi * self.radius)


circy = Circle(4.44)
circy.get_area()
print(circy.get_area())

circy.get_perimeter()
print(circy.get_perimeter())
