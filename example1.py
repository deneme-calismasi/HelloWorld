class MyClass():
    def _len_(self):
        return 0


myObj = MyClass()
print(bool(myObj))


class Foo(object):
    def _init_(self, obs=[0, 1, 2]):
        self.data = obs
        self.max = max(obs)
        self.min = min(obs)
        self.len = len(obs)
        print(max(obs))


tuple1 = ("apple", "banana", 12)
if type(tuple1) == str:
    print("all items are string")
elif type(tuple1) == tuple:
    print("all items are tuple")
