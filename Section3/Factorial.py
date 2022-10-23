def fact(n):
    facto = 1
    for i in range(2, n + 1):
        facto *= i
    return facto

def fact(n):
    def fact(n, r):
        if n < 2:
            return r
        else:
            return fact(n-1,r*n)
    return fact(n, 1)