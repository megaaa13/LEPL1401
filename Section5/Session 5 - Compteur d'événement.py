def count(events, i, j):
    k = (i, j)
    occurences = 0
    for i in events:
        if i == k:
            occurences += 1
    return occurences
