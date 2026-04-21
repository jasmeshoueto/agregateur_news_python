from scraper.scraper import Scraper

class Aggregator:
    """Coordonne plusieurs scrapers et filtre les articles par mots-clés."""

    def __init__(self,mots_cles):
        self.mots_cles = [mot.lower() for mot in mots_cles]
        self.scrapers = []
        self.articles = []

    def ajouter_source(self, nom_source, url):
            """Ajoute un site de presse à scraper."""
            self.scrapers.append(Scraper(nom_source, url))

    def collecter_tous(self):
        """Lance la collecte sur tous les sites."""
        self.articles = []
        for scraper in self.scrapers:
            articles = scraper.collecter()
            self.articles.extend(articles)
        return self.articles

    def filtrer(self):
        """Retourne les articles contenant un mot-clé."""
        resultat = []
        for article in self.articles:
            titre_lower = article.titre.lower()
            for mot in self.mots_cles:
                if mot in titre_lower:
                    resultat.append(article)
                    break
                    return resultat 