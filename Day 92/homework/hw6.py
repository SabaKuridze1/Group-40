def g_first(a):
    def g_first_key(word):
        if len(word) > 0 and word[0] == 'g':
            return 0
        else:
            return 1

    sorted_words = sorted(a, key=g_first_key)
    return sorted_words




print(g_first(["a", "gamarjoba", "salami"]))