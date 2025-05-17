def reverse_words(s):
    s = s.split()
    s = s[::-1]
    return ' '.join(s)