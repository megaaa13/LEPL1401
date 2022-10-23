a = ... #variable à évaluer
b = ... #variable à évaluer
rest = ... #enregistrez dans cette variable le reste de la division a/b

c = a
rest = 0
if b == 0:
    rest = None
while rest == 0:
    if (c - b) >= 0:
        c = c - b
    else:
        rest = c
        c = 0
        print(rest)
        break