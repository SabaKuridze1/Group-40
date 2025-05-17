def is_isogram(string):
    string = string.lower()
    seen_letters = []
    for letter in string:
        if letter in seen_letters:
            return False
        seen_letters.append(letter)
    return True