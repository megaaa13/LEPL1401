from turtle import position
from QBF import *
import bioinfo
assert position("ab", "CDEF") == [], "Valeur à ne pas trouver"
assert position("?B", "CAbDEF") == [1], "Test ? Première pos"
assert position("A?", "CABDEACF") == [1, 5], "Test ? 2ème pos"
assert position("aa", "CAAABDEAAF") == [1, 2, 7], "Test avec doublon aa"
assert position("??", "CAAAB") == [0, 1, 2, 3], "Test avec que des ??"
assert bioinfo.is_adn("AGCTAGG"), "Doit retourner True, il retourne False"

a = bioinfo.positions("aaA", "aa")
print(bioinfo.positions("aaa", "aa"))