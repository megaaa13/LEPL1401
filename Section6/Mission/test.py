from assistant import *

""" Pour utiliser ce test de l'assistant, veuillez disposer
des fichiers error1.txt, error2.txt
    Ici c'est une version modifié de l'assistant qu'on teste, les fonctions utilisent des return au lieu de print
    De plus les fonctions exit et help ne sont pas testées"""


def test_file():
    assert file("error1") == "File not found !", "Test1 file"
    assert file("error1.txt") == "File error1.txt loaded !", "Test2 file"
    assert file("error2.txt") == "File error2.txt loaded !", "Test3 file"
    print('Test passed !')


def test_info():
    assert info() == "Please load a file before !"
    file("error2.txt")
    assert info() == "File : error2.txt\n6 lines\n47 caracters", "Test2 info"
    print('Test passed !')


def test_dictionary():
    file("error1.txt")
    assert dictionary() == "error1.txt is now used as dictionary !", "Test1"
    file("error2.txt")
    assert dictionary() == "error2.txt is now used as dictionary !", "Test2"
    print('Test passed !')


def test_search():
    file("error1.dat")
    assert search(
        "zeee (the prononcé à la française)") == "zeee (the prononcé à la française) is not in the dictionary", "Test1"
    assert search("the") == "the is in the dictionary", "Test2"
    assert search("those") == "those is in the dictionary", "Test3"
    file("error2.dat")
    assert search("these") == "these is in the dictionary", "Test4"
    print('Test passed !')


def test_sum():
    assert sum("1+4+5") == 10, "Test1"
    assert sum("1+4 ") != 10, "Test2"
    print('Test passed !')


def test_avg():
    assert avg("1+5+3", 3) == 3.0, "Test1"
    assert avg("4+5+786", 3) != 266, "Test2"
    print('Test passed !')


test_info()
test_dictionary()
test_avg()
test_sum()
test_file()
test_search()
