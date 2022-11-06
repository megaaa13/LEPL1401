def create_index(list_of_words):
    dict = {}
    for n, i in enumerate(list_of_words):
        tmp = dict.get(i, [])
        tmp.append(n)
        dict[i] = tmp
    return dict

def create_index_understandable(list_of_words):
    dict = {}
    for i in range(len(list_of_words)):
        tmp = dict.get(list_of_words[i], [])
        tmp.append(i)
        dict[list_of_words[i]] = tmp
    return dict

print(create_index_understandable(["the","galaxy","and","the","universe","are","the","same"]))