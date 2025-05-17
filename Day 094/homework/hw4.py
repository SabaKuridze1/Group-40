def vaporcode(s):
    result = []
    for char in s:
        if char != ' ':
            result.append(char.upper())
    return '  '.join(result)