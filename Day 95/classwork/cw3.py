def solution(s):
    res = ""
    for i in s:
        if i == i.upper():
            res += f" {i}"
        else:
            res += i
    return res