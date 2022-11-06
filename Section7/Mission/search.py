import re


def readfile(filename):
    """Permet de transformer un fichier en liste de lignes

    :param filename: Nom du fichier à traiter
    :return: Liste contenant les lignes
    """
    try:
        with open(filename, "r") as file:
            fichier = []
            for line in file.readlines():
                fichier.append(line.strip())
        return fichier
    except FileNotFoundError:
        return []


def get_words(line):
    """Transforme une string en liste de mot

    :param line: La ligne à séparer en mots
    :return: Une liste contenant des strings (mots)
    """
    if not line:
        return []
    words = []
    sans_ponc = line.translate(str.maketrans("", "", r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")).strip().lower()
    # On retire toute la ponctuations des mots
    for word in re.split(" +|\t+|'+", sans_ponc):
        # Coupe la phrase en mots, au niveau des espaces,
        # tabulations et apostrophes.
        words.append(word)
    return words


def create_index(filename):
    """Crée un dictionnaire de tous les mots compris dans le fichier à traiter

    :param filename: Nom du fichier à traiter
    :return: dictionnaire contenant des sous dictionnaires des occurences des mots selon les phrases.
    """
    dico = {}
    for index, ligne in enumerate(readfile(filename)):
        for mot in get_words(ligne):
            if mot not in dico:  # On check si le mot est déjà dans l'index principal
                dico[mot] = {}
            if index not in dico[mot]:  # On la ligne si le mot est déjà référencé dans l'index du mot
                dico[mot][index] = 0
            dico[mot][index] += 1
    return dico


def get_lines(words, index: dict):
    """Permet de trouver les lignes communes où les mots choisis apparaissent en même temps.

    :param words: Liste de mots dont il faut trouver une des lignes communes
    :param index: Dictionnaire contenant les mots et les lignes où ils apparaissent
    :return: Liste des lignes où les mots apparaissent ensemble
    """
    sous_dico, result = [], []
    for word in words:
        sous_dico.append(index.get(word.lower(), 0))  # On récupère les indexs de chaque mot
        if 0 in sous_dico:  # Si l'exception est déclarée, c'est qu'un des mots n'est pas dans l'index
            return []
    for i in sous_dico[0]:
        for j in sous_dico:
            if i not in j:
                break
        else:
            result.append(i)
    return result


if __name__ == '__main__':  # Fonction ne s'exécutant que si on run le fichier, pour éviter un problème lors des tests
    print("Choose a file :")
    while True:
        entry = input("> ")
        if entry == "exit":
            raise SystemExit
        try:
            open(entry, "r")
        except FileNotFoundError:
            print("File not found !")
        else:
            name = entry
            break
    print("Choose the words to check !")
    while True:
        entry = input("> ")
        if entry == "exit":
            raise SystemExit
        line = get_words(entry)
        if line:
            print(get_lines(line, create_index(name)))
        else:
            print("Please choose words !")
