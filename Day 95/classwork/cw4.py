def generate_hashtag(s):
    if s == "":
        return False
    
    words = s.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    
    joined = "".join(capitalized_words)
    result = f"#{joined}"
    
    if len(result) > 140:
        return False
    
    return result