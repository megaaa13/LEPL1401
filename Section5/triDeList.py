def merge(first_list, second_list):
    lst = first_list + second_list
    lst.sort(key=lambda x: x[1])
    return lst