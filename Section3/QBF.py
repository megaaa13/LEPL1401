def chiffres_pairs(n):
    s = n
    i = 0
    while s >= 1:
        i += 1
        s /= 10
    return True if i % 2 == 0 and i != 0 else False