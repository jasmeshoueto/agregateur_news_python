import requests
from bs4 import BeautifulSoup
from scraper.article import Article
class Scraper:
    """Récupère les articles depuis un site de presse."""

    def __init__(self,nom_source,url):
        self.nom_source = nom_source
        self.url = url  

    def collecter(self):
        """"Collecte les articles du site via le flux RSS"""
        articles = []
        try:
            headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(self.url,timeout=60, headers=headers)
            soup = BeautifulSoup(response.content, "xml")
            items=soup.find_all("item")

            for item in items:
                titre = item.find("title")
                lien = item.find("guid")
                if titre and lien:
                    titre_propre = " ".join(titre.get_text(strip=True).split())
                    lien_propre =" ".join(lien.get_text(strip=True).split())
                    articles.append(Article(
                        titre_propre,
                        lien_propre,
                        self.nom_source
                    ))
            return articles
        except requests.exceptions.RequestException as e:
                            print(f"Erreur de connexion sur {self.nom_source} : {e}")
