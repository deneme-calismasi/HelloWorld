"""
fruits = ["banana", "melon", "apple"]
for x in fruits:
    print(x + "\n")

cars = ["Ford", "Renault", "Audi"]
for x in cars:
    if x == "Renault":
        break
    print(x + "\n")
for x in cars:
    if x == "Audi":
        print(x + "\n")
        break

"""

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for x in numbers:
    sum = sum+x

print("The sum is", sum)