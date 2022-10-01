for i in range(1, n+1):
    div = 0
    for j in range(1,i):
        div = div + 1 if i%j == 0 else div
    print(f"{i} : {div}")