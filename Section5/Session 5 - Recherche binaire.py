def binary_search(course, list_of_courses):
    first, last = 0, len(list_of_courses) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if list_of_courses[middle][0] == course:
            found = True
        elif course < list_of_courses[middle][0]:
            last = middle - 1
        else:
            first = middle + 1
    if found:
        return list_of_courses[middle][1]
    elif not found:
        return []


print(binary_search("LINFO1111", [('LINFO1101', ['Jean', 'Pierre']), ('LINFO1110', ['Jean']), ('LINFO1111', ['Jean']),
                                  ('LINFO1112', ['Jacques', 'Pierre']), ('LINFO1113', ['Pierre'])]))
