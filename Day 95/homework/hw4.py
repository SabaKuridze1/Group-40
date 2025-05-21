def find_it(seq):
    new_list = []
    for char in seq:
        if seq.count(char) % 2 != 0:
            new_list.append(char)
    return new_list[0]
        