def expanded_form(num):
    num_str = str(num)
    result = []

    for i in range(len(num_str)):
        digit = num_str[i]
        if digit != "0":
            zeros = len(num_str) - i - 1
            result.append(digit + "0" * zeros)

    return " + ".join(result)