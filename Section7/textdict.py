def create_dictionary(filename):
    with open(filename, "r") as file:
        dico = {}
        for i in file:
            for j in i.split(" "):
                dico[j] = dico.get(j, 0) + 1
    return dico
def occ(dictionary, word): return dictionary.get(word, 0)