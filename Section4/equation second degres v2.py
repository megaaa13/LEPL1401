def solveur(lst):
    arr = []
    if len(lst) == 0: return arr
    for i in lst:
        arr.append(solution(i[0], i[1], i[2]))
    return arr


solveur([[1, 1, -1], [4, 4, 1], [1, 2, 3], [-1, 2, 3]])