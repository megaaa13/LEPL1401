def is_adn(text):
    """pre: text : string
    \n post: si la séquence est de l'adn"""
    if text == "":
        return False
    for i in text:
        if i.lower() not in ["a", "c", "g", "t"]:
            return False
    return True


def positions(text, car):
    """pre: text : string, car : string (mais plus petite)
    post: retourne la position de car dans text"""
    pos = []
    for i in range(len(text)):
        ok = True
        if text[i].lower() == car[0].lower():
            for j in range(len(car)):
                if i + j >= len(text):
                    ok = False
                    break
                if car[j].lower() != text[i + j].lower():
                    ok = False
                    break
            if ok:
                pos.append(i)
    return pos


def distance_h(text1, text2):
    """pre: text1, text2, strings
    \npost : retourne la distance de haming des 2 strings"""
    diff = 0
    if len(text1) != len(text2):
        return None
    for i in range(len(text1)):
        if text1[i].lower() != text2[i].lower():
            diff += 1
    return diff


def distances_matrice(l):
    """pre: l: list de string
    \npost: retourne une matrice des distances de haming pour une liste donnée"""
    matrix = []
    for i in l:
        r = []
        for j in range(len(l)):
            r.append(distance_h(i, l[j]))
        matrix.append(r.copy())
    return matrix
