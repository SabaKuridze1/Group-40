def descending_order(num):
    str_num = str(num)
    new_list = []
    result = ""
    
    for i in str_num:
        new_list.append(i)
        sort = sorted(new_list, reverse = True)
        
    for x in sort:
        result += x
        
    return int(result)