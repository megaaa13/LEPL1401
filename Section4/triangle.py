def triangle(n):
    x = []
    y = []
    for i in range(n+1):
        y.append(i)
        x.append(y.copy())
    return x


print(triangle(2), sep="\n")
