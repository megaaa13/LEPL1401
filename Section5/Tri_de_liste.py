def sorteda(a_list):
    sorted_list = [a_list[0]]
    for i in a_list:
        for j in range(len(sorted_list)):
            if len(sorted_list) == 1:
                if sorted_list[0] < i:
                    sorted_list.append(i)
                    break
                elif sorted_list[0] > i:
                    sorted_list.insert(0, i)
                    break
            if sorted_list[len(sorted_list) - 1] < i:
                sorted_list.append(i)
                break
            elif sorted_list[0] > i:
                sorted_list.insert(0, i)
                break
            elif sorted_list[j] < i < sorted_list[j + 1]:
                sorted_list.insert(j + 1, i)
                break
            elif i == sorted_list[j]:
                sorted_list.insert(j, i)
                break
    sorted_list.remove(a_list[0])
    return sorted_list


assert sorteda([18, 18, 83, 47, 19, 62, 97, 10, 94, 44, 29, 8, 13, 16, 90, 18, 93, 40, 69]) == \
       [8, 10, 13, 16, 18, 18, 18, 19, 29, 40, 44, 47, 62, 69, 83, 90, 93, 94, 97], \
    sorted([18, 18, 83, 47, 19, 62, 97, 10, 94, 44, 29, 8, 13, 16, 90, 18, 93, 40, 69])
