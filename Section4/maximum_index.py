def maximum_index(lst):
    if len(lst) == 0:
        return None
    t = 0
    y = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > y:
            t = i
            y = lst[i]
    return t


print(maximum_index([1,3,3]))
