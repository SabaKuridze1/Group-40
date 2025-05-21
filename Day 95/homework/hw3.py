def compute_sum(n):
    sum = 0

    for i in range(1, n + 1):
        str_num = str(i)

        for ch in str_num:
            digit = int(ch) 
            sum += digit   

    return sum