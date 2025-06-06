def even_fib(n):
    x, y = 0, 1
    counter = 0
    while y < n:
        if y % 2 == 0:
            counter += y
        x, y = y, x + y
    return counter