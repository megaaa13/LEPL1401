##############################
# Tests pour la classe Duree #
##############################
from mission8 import Duree, Chanson, Album


def test_Duree_str(duree1, duree2):
    assert duree1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert duree2.__str__() == "08:41:25", "Test 2 Duree __str__"


def test_Duree_to_secondes(duree1, duree2):
    assert duree1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert duree2.to_secondes() == 31285, "Test 2 Duree toSecondes"


def test_Duree_delta(duree1, duree2):
    assert duree1.delta(duree2) < 0, "Test 1 Duree delta"
    assert duree2.delta(duree1) > 0, "Test 2 Duree delta"


def test_Duree_apres(duree1, duree2):
    duree0 = Duree(0, 0, 0)
    assert duree1.apres(duree2), "Test 1 Duree apres"
    assert not duree0.apres(duree1), "Test 2 Duree apres"
    # A COMPLETER PAR LES ETUDIANTS


def test_Duree_ajouter(duree1, duree2):
    duree0 = Duree(0, 0, 0)
    duree0.ajouter(duree1)
    assert str(duree0) == str(duree1), "Test 1 Duree ajouter"
    duree1.ajouter(duree2)
    assert str(duree1) == "19:02:24", "Test 2 Duree ajouter"


d1 = Duree(10, 20, 59)
d2 = Duree(8, 41, 25)
test_Duree_str(d1, d2)
test_Duree_to_secondes(d1, d2)
test_Duree_delta(d1, d2)
test_Duree_apres(d1, d2)
test_Duree_ajouter(d1, d2)


################################
# Tests pour la classe Chanson #
################################
def test_Chanson_str():
    assert c.__str__() == "Let's Dance - David Bowie - 00:04:05", "Test 1 str chanson"
    assert c1.__str__() == "Never Gonna Give You Up - Rick Astley - 00:03:32", "Test 2 str chanson"


c = Chanson("Let's Dance", "David Bowie", Duree(0, 4, 5))
c1 = Chanson("Never Gonna Give You Up", "Rick Astley", Duree(0, 3, 32))
test_Chanson_str()


##############################
# Tests pour la classe Album #
##############################
def str_Album(album):
    assert album.__str__() == "Album 1 (2 chansons, 00:07:37)\n" \
                              "01: Never Gonna Give You Up - Rick Astley - 00:03:32\n" \
                              "02: Let's Dance - David Bowie - 00:04:05\n", "Test str album"


def add_Album(album):
    assert str(album) == "Album 2 (0 chansons, 00:00:00)\n", "Test add 1"
    album.add(Chanson("Never Gonna Give You Up", "Rick Astley", Duree(0, 3, 32)))
    assert str(album) == "Album 2 (1 chansons, 00:03:32)\n" \
                         "01: Never Gonna Give You Up - Rick Astley - 00:03:32\n", "Test add 2"


a = Album(1)
a.add(Chanson("Never Gonna Give You Up", "Rick Astley", Duree(0, 3, 32)))
a.add(Chanson("Let's Dance", "David Bowie", Duree(0, 4, 5)))
alb = Album(2)
str_Album(a)
add_Album(alb)
#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# (A COMPLETER PAR LES ETUDIANTS)
