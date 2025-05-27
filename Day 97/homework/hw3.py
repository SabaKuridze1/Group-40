def nickname_generator(name):
    vowels = "aeiou"
    if len(name) < 4:
        return "Error: Name too short"
    elif name[2] not in vowels: 
        return name[:3]
    elif name[2] in vowels:
        return name[:4]