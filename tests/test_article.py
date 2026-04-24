from scraper.article import Article
from scraper.aggregator import Aggregator
from scraper.storage import Storage
import os


# Test 1 : Création d'un article
def test_creation_article():
    article = Article("Titre test", "http://test.com", "BBC")
    assert article.titre == "Titre test"
    assert article.lien == "http://test.com"
    assert article.source == "BBC"


# Test 2 : Affichage d'un article
def test_affichage_article():
    article = Article("Titre test", "http://test.com", "BBC")
    assert "BBC" in article.source
    assert "Titre test" in article.titre


# Test 3 : Aggregator filtre correctement
def test_filtrage():
    aggregateur = Aggregator(["python"])
    article1 = Article("Python is great", "http://test.com", "BBC")
    article2 = Article("Football match", "http://test2.com", "CNN")
    aggregateur.articles = [article1, article2]
    resultats = aggregateur.filtrer()
    assert len(resultats) == 1
    assert resultats[0].titre == "Python is great"


# Test 4 : Aggregator avec mot-clé absent
def test_filtrage_vide():
    aggregateur = Aggregator(["javascript"])
    article1 = Article("Python is great", "http://test.com", "BBC")
    aggregateur.articles = [article1]
    resultats = aggregateur.filtrer()
    assert len(resultats) == 0


# Test 5 : Sauvegarde JSON
def test_sauvegarde_json():
    articles = [Article("Test", "http://test.com", "BBC")]
    storage = Storage("data/test.json", format="json")
    storage.sauvegarder(articles)
    assert os.path.exists("data/test.json")