def expand_string(s):
    result = ""
    repeat = 1

    for char in s:
        if '0' <= char <= '9':
            repeat = int(char) 
        else:
            result += char * repeat 
    return result