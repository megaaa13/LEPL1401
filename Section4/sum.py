def sum(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += i
    return sum