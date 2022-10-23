from math import *


def rho(a, b, c):
    return b ** 2 - 4 * a * c


def n_solutions(a, b, c):
    if rho(a, b, c) > 0:
        return 2
    elif rho(a, b, c) == 0:
        return 1
    else:
        return 0


def solution(a, b, c):
    if n_solutions(a, b, c) == 2:
        first = ((- b) - (sqrt(rho(a, b, c)))) / (2 * a)
        second = ((- b) + (sqrt(rho(a, b, c)))) / (2 * a)
        return min(first, second)
    elif n_solutions(a, b, c) == 1:
        return - b / (2 * a)


print(solution(-1, 2, 3))
