def interests(base, y, x):
    montant = base
    for i in range(x):
        montant += montant * y / 100
    return montant