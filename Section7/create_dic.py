l = [(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]


def create_dict(lst):
    d = {}
    seen = []
    for i in lst:
        if i[0] not in seen:
            d[i[0]] = []
            seen.append(i[0])
            d[i[0]].append(i[1])
        else:
            d[i[0]].append(i[1])
    return d

def create_dict_better(l):
    d = {}
    for tuple in l:
        l = d.get(tuple[0], [])
        l.append(tuple[1])
        d[tuple[0]] = l
    return d

def create_dict_max_better(l):
    d = {}
    for i in l:
        e = d.get(i[0], 0)
        if i[1] > e:
            d[i[0]] = i[1]
    return d

def create_dict_max(lst):
    d = {}
    for i in lst:
        if i[0] not in d:
            d[i[0]] = i[1]
        else:
            if d[i[0]] < i[1]:
                d[i[0]] = i[1]
    return d
