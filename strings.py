# Multiline Strings

a = """ This 
is 
a
multiline strings """

for x in "banana":
    print(x)

b = "Hello World"
print(len(b))

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present")

# len with sequence
print('string length =', len('abc'))  # string
print('tuple length =', len((1, 2, 3)))  # tuple
print('list length =', len([1, 2, 3, 4]))  # list
print('bytes length =', len(bytes('abc', 'utf-8')))  # bytes
print('range length =', len(range(10, 20, 2)))  # range

# len with collections
print('dict length =', len({"a": 1, "b": 2}))  # dict
print('set length =', len(set([1, 2, 3, 3])))  # set
print('frozenset length =', len(frozenset([1, 2, 2, 3])))  # frozenset
