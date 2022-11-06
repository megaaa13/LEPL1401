f = [[0, 2, 4], [4, 1, 0]]
w = {(0, 1): 2, (0, 2): 4, (1, 0): 4, (1, 1): 1}


def equal(l, d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != 0:
                if (i, j) in d:
                    if d[(i, j)] != l[i][j]:
                        return False
                else:
                    return False
    return True


print(equal(f, w))
