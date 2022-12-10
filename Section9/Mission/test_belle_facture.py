from mission9 import Article, Facture, ArticleReparation, ArticlePiece, Piece
from PIL import Image, ImageDraw

img = Image.new('RGB', (530, 800), color="#FFFFFF")


class TestArticleInitial:
    articles = [Article("laptop 15\" 8GB RAM", 743.79),
                Article("installation windows", 66.11),
                Article("installation wifi", 45.22),
                Article("carte graphique", 119.49),
                ArticleReparation(0.75),
                ArticlePiece(3, Piece("Sofa", 12.99, 120, False, False)),
                ArticlePiece(3, Piece("Coussins", 12.99, 0.3, False, True)),
                ArticlePiece(356, Piece("Ciment", 26.95, 10, True, True)),
                ArticlePiece(3, Piece("PS5", 499.99, 1.5, True, False))
                ]

    @classmethod
    def run(cls):
        for art in cls.articles:
            print(art)


class TestFactureInitial:
    facture = Facture("PC Store - 22 novembre", TestArticleInitial.articles)
    pixel = 10

    @classmethod
    def run(cls):
        print(cls.facture)
        print(cls.facture.livraison_str())
        d = ImageDraw.Draw(img)
        d.text((10, TestFactureInitial.pixel), str(cls.facture), fill="#000000")
        TestFactureInitial.pixel += 60 + 15 * len(TestArticleInitial.articles) + 45 + 10
        d.text((10, TestFactureInitial.pixel), str(cls.facture.livraison_str()), fill="#000000")
        TestFactureInitial.pixel += 60 + 15 * cls.facture.nbr_livr() + 55 + 10


if __name__ == "__main__":
    print("*** TEST DE LA CLASSE Article ***")
    print()
    TestArticleInitial.run()

    print()
    print("*** TEST DE LA CLASSE Facture ***")
    print()
    TestFactureInitial.run()
    img.save("facture.jpg")
