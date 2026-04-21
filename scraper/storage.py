import json
import csv
from scraper.article import Article

class Storage:
    """Sauvegarde et charge les articles en JSON ou CSV."""

    def __init__(self, chemin_fichier,format="json"):
        self.chemin_fichier = chemin_fichier
        self.format =format

    def sauvegarder(self, articles):
        """Sauvegarde une liste d'articles dans un fichier."""
        if articles is None:
            articles = []
        if self.format == "json":
            self._sauvegarder_json(articles)
        elif self.format == "csv":
            self._sauvegarder_csv(articles)

    def _sauvegarder_json(self, articles):
        data = [{"titre": a.titre, "lien": a.lien, "source": a.source} for a in articles]
        with open(self.chemin_fichier, "w",encoding="utf-8")as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Sauvegarde JSON: {self.chemin_fichier}")

    def _sauvegarder_csv(self):
        """Sauvegarde en CSV."""
        with open(self.chemin_fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["titre", "lien", "source"])
            for a in articles:
                writer.writerow([a.titre, a.lien, a.source])
        print(f"Sauvegarde CSV: {self.chemin_fichier}")

    def charger_json(self):
        try:
            with open(self.chemin_fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Article(d["titre"], d["lien"], d["source"]) for d in data]
        except FileNotFoundError:
            print("Fichier introuvable.")
            return []
                                    
                    