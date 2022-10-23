def average(list):
    a = 0
    if len(list) == 0: return None
    for i in list:
        a += i
    return a / len(list)