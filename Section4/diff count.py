def diff_count(lst: list):
    """pre : lst : list
    \n post : int (longueur de l'array contenant seulement des nombres uniques
    """
    lst1 = []
    for i in lst:
        if not (i in lst1):
            lst1.append(i)
    return len(lst1)


print(diff_count([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 7, 9]))
