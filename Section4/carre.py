def carre(n):
    x = []
    y = []
    for m in range(1, n + 1):
        y.clear()
        for i in range(n * (m - 1), n * m):
            y.append(i)
        x.append(y.copy())
    return x


#print(carre(6))
