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


print(treatment("number number number consonant-up consonant-up vowel-up vowel-low consonant-up consonant-up number "
                "number"))
