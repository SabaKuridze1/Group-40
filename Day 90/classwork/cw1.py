def duplicate_count(text):
    low = text.lower()
    duplicates = []
    for letter in low:
        if low.count(letter) > 1 and letter not in duplicates:
            duplicates.append(letter)
    return len(duplicates)