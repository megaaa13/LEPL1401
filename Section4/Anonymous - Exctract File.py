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


print(extract("4E3e5t6"))
