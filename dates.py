import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.date())
print(x.strftime("%D"))
print(x.strftime("%A"))


name = "John"
print("Hello, %s!" % name)

name = 123
print("Hello, %s!" % name)