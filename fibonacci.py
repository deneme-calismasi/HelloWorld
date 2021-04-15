def fib(n):
    a, b, c = 0, 1, 2
    while a < n:
        print(a, end=' ')
        a, b, c = b, a + b, b + c


fib(1000000)
