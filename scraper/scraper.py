import requests
from bs4 import BeautifulSoup
from scraper.article import Article


class Scraper:

    def __init__(self, nom_source, url):
        self.nom_source = nom_source
        self.url = url

    def collecter(self):
        articles = []
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            response = requests.get(self.url, timeout=10, headers=headers)
            soup = BeautifulSoup(response.content, "xml")
            items = soup.find_all("item")
            for item in items:
                titre = item.find("title")
                description = item.find("description")
                guid = item.find("guid")
                if titre and guid:
                    titre_propre = " ".join(titre.get_text(strip=True).split())
                    description_propre = " ".join(description.get_text(strip=True).split()) if description else ""
                    guid_text = guid.get_text(strip=True)
                    if guid_text.startswith("http"):
                        lien_propre = guid_text
                    else:
                        lien_propre = "https://www.france24.com/fr/" + guid_text
                    articles.append(Article(
                        titre_propre,
                        lien_propre,
                        self.nom_source,
                        description_propre
                    ))
        except requests.exceptions.RequestException as e:
            print(f"Erreur sur {self.nom_source} : {e}")
        return articles