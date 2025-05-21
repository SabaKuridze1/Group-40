def encode(st):
    res = ""
    for i in st:
        if i == "a":
            res += "1"
        elif i == "e":
            res += "2"
        elif i == "i":
            res += "3"
        elif i == "o":
            res += "4"
        elif i == "u":
            res += "5"
        else:
            res += i
    return res
def decode(st):
    res1 = ""
    for i in st:
        if i == "1":
            res1 += "a"
        elif i == "2":
            res1 += "e"
        elif i == "3":
            res1 += "i"
        elif i == "4":
            res1 += "o"
        elif i == "5":
            res1 += "u"
        else:
            res1 += i
    return res1