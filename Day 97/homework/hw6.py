def to_camel_case(text):
    text = text.replace("_", "-")
    split = text.split('-')

    result = [split[0]]  

    for elem in split[1:]: 
        result.append(elem.capitalize())

    return "".join(result)