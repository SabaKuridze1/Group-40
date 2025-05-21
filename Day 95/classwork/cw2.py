def spin_words(sentence):
    sentence = sentence.split()
    new_list = []
    for word in sentence:
        if len(word) >= 5:
            new_list.append(word[::-1])
        else:
            new_list.append(word)
            
    return " ".join(new_list)
    