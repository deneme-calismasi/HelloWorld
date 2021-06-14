class Student:
    name = "GeekForGeeks"

    def print_name(self):
        print("The name is", self.name)


Student.print_name = classmethod(Student.print_name)

Student.print_name()
