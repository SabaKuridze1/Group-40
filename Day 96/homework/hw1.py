def digital_root(n):
    while n >= 10:
        str_n = str(n)
        sum = 0
        for i in str_n:
            sum += int(i)
        n = sum
    return n