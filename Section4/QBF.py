def position(s, t):
    pos = []
    for i in range(len(t)):
        ok = True
        if t[i].lower() == s[0].lower() or s[0] == "?":
            for j in range(len(s)):
                if i + j >= len(t):
                    ok = False
                    break
                if t[i + j].lower() != s[j].lower() and s[j] != "?":
                    ok = False
                    break
            if ok:
                pos.append(i)
    return pos


def positions(n, s):
    ok = []
    for i in range(len(s)):
        if s[i].lower() == n[0].lower() or n[0].lower() == "?":
            for j in range(len(n)):
                if i + j == len(s):
                    break
                if s[i + j].lower() != n[j].lower() and n[j] != "?":
                    break
            else:
                ok.append(i)
    return ok


print(positions("ab", "CDEF"))
print(positions("?B", "CAbDEF"))
print(positions("A?", "CABDEACF"))
print(positions("aa", "CAAABDEAAF"))
print(positions("??", "CAAAB"))
