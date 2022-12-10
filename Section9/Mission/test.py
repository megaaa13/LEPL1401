"""
    Tests fournis pour la mission 9; à compléter par les étudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

from mission9 import Article, Facture, ArticleReparation, ArticlePiece, Piece

"""
   Classe de test initiale pour la classe Article.
   @author Kim Mens
   @version 18 novembre 2018
"""


class TestArticleInitial:
    articles = [Article("laptop 15\" 8GB RAM", 743.79),
                Article("installation windows", 66.11),
                Article("installation wifi", 45.22),
                Article("carte graphique", 119.49),
                ArticleReparation(0.75),
                ArticlePiece(3, Piece("Sofa", 12.99, 120, False, False)),
                ArticlePiece(3, Piece("Coussins", 12.99, 0.3, False, True)),
                ArticlePiece(356, Piece("Ciment", 26.95, 10, True, True))
                ]

    @classmethod
    def run(cls):
        for art in cls.articles:
            print(art)


class TestFactureInitial:
    facture = Facture("PC Store - 22 novembre", TestArticleInitial.articles)

    @classmethod
    def run(cls):
        print(cls.facture)
        print(cls.facture.livraison_str())


if __name__ == "__main__":
    print("*** TEST DE LA CLASSE Article ***")
    print()
    TestArticleInitial.run()

    print()
    print("*** TEST DE LA CLASSE Facture ***")
    print()
    TestFactureInitial.run()
