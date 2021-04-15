class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printidentity(self):
        print(self.fname, self.lname)


person1 = Person("Ali", "Yilmaz")
person2 = Person("Veli", "Ozturk")
person1.printidentity()
person2.printidentity()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)


student1 = Student("Mike", "Olsen", 2018)
student1.printidentity()
print(student1.graduationyear)

student1.welcome()
