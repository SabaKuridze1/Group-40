def pig_it(text):
    sityvebi = text.split()
    shedegi = []
    for sityva in sityvebi:
        if sityva.isalpha():
            shedegi.append(sityva[1:] + sityva[0] + "ay")
        else:
            shedegi.append(sityva)
            
    return ' '.join(shedegi)