def feast(beast, dish):
    beast = beast.split()
    dish = dish.split()
    if dish[0] == beast[0] and dish[-1] == beast[-1]:
        return True
    else:
        return False
