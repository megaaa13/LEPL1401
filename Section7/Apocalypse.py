def extract(code: str):
    codex = ''
    for i in range(len(code)):
        if code[i].isnumeric():
            codex += "number "
        elif code[i].lower() in ["a", "e", "i", "o", "u", "y"]:
            if code[i].islower():
                codex += "vowel-low "
            else:
                codex += "vowel-up "
        else:
            if code[i].islower():
                codex += "consonant-low "
            else:
                codex += "consonant-up "
    return codex

def translate(data):
    translateur = ""
    for i in data:
            if i.lower() not in "abcdefghijklmnopqrstuvwyxz0123456789":
                raise ValueError
            translateur += morse[i]
    return translateur

def translate_other(data, lan):
    d = data.split(" ")
    s = []
    for i in d:
        s.append(lan.get(i.lower(), i))
    return " ".join(s)

def treatment(data: str):
    codex = data.split()
    dupli = []
    treated = ''
    for i in range(len(codex)):
        multi = 1
        if i not in dupli:
            for j in range(i+1, len(codex)):
                if codex[i] == codex[j]:
                    multi += 1
                    dupli.append(j)
                else:
                    break
            if i != 0 :
                treated += " "
            treated = treated + codex[i] + "*" + str(multi)
    return treated


def collect(file):
    try:
        with open(file, "r") as file:
            occ = {}
            for line in file:
                f = treatment(extract(line.strip()))
                if f not in occ:
                    occ[f] = 0
                occ[f] += 1
        return occ
    except:
        raise FileNotFoundError
