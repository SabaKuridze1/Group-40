def print_array(arr):
    listn = []
    
    for i in arr:
        str_i = str(i)
        listn.append(str_i)
    
    result = ",".join(listn)
    return result