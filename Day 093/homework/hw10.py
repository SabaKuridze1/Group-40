def alphabet_position(text):
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    lis = [] 
    
    for i in text:
        if i in upper_alpha:
            index = upper_alpha.index(i) + 1
            lis.append(str(index))
        elif i in lower_alpha:
            index = lower_alpha.index(i) + 1
            lis.append(str(index)) 
    return " " .join(lis)