def greatest_divisor(a):
    div = None
    for i in range(1,a):
        if a == 1:
            return div
        if a % i == 0:
            div = i
    return div