class Website:
    def __init__(self, title, a):
        self.title = title
        self.a = a

    def show_title(self, b):
        print(self.title)
        self.a = 10 * 12
        b = b * 10
        print(b, self.a)
        print(self.a)
        return self.a, b


obj = Website("basicpython.org", 12).show_title(10)
