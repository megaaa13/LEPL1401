def fibonacci(n):
    v0, v1 = 0,1
    if n == 0: return 0
    for i in range(n-1):
        v0, v1 = v1, v0+v1
    return v1

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(12))
