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
                titre_tag = item.find("title")
                resume_tag = item.find("description") 
                guid = item.find("guid")
                lien_tag = item.find("link")
                if titre_tag :
                    titre = titre_tag.get_text(strip=True) if titre_tag else ""
                    resume = BeautifulSoup(resume_tag.get_text(), "html.parser").get_text(strip=True) if resume_tag else ""
                    if lien_tag and lien_tag.next_sibling:
                        lien =str(lien_tag.next_sibling).strip()
                    elif guid:
                        lien = guid.get_text(strip=True).split("#")[0]
                    else:
                        lien = ""
                    articles.append(Article(
                        titre,
                        lien,
                        self.nom_source,    
                        resume
                    ))
        except requests.exceptions.RequestException as e:
            print(f"Erreur sur {self.nom_source} : {e}")
        return articles
