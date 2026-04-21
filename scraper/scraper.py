import requests
from bs4 import BeautifulSoup
from scraper.article import Article
class Scraper:
    """Récupère les articles depuis un site de presse."""

    def __init__(self,nom_source,url):
        self.nom_source = nom_source
        self.url = url  

    def collecter(self):
        """"Collecte les articles du site et retourne une liste d'articles."""
        articles = []
        try:
            response = requests.get(self.url,timeout=6)
            soup = BeautifulSoup(response.text, 'html.parser')
            titres=soup.find_all("a")

            for tag in titres:
                titre = tag.get_text(strip=True)
                lien = tag.get("href", "")
                if titre and lien.startswith("http"):
                    articles.append(Article(titre, lien, self.nom_source))

        except requests.exceptions.RequestException as e:
                            print(f"Erreur de connexion sur {self.nom_source} : {e}")
        return articles

                