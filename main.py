from scraper.aggregator import Aggregator
from scraper.storage import Storage

print("===Agrégateur de News Personnalisé ====\n")

# 1. Saisie des mots-clés
mots_cles = input("Entrez vos mots-clés  (séparés par des virgules) : ")
mots_cles = [mot.strip() for mot in mots_cles.split(",") ]

# 2. Création de l'agrégateur
aggregator = Aggregator(mots_cles)

# 3. Ajout des sources
aggregator.ajouter_source("Le Monde", "https://www.lemonde.fr/rss/une.xml")
aggregator.ajouter_source("Le Figaro", "https://www.lefigaro.fr/rss/figaro_actualites.xml")
aggregator.ajouter_source("France 24", "https://www.france24.com/fr/rss")
aggregator.ajouter_source("BBC News", "https://feeds.bbci.co.uk/news/rss.xml")



# 4. Collecte des articles
print("\nCollecte des articles...")
aggregator.collecter_tous()

# 5. Filtrage
resultats = aggregator.filtrer()



# 6. Affichage
if resultats:
    print(f"{len(resultats)} article(s) trouvé(s):\n")
    for article in resultats :
        print(f"Source: {article.source}, Titre: {article.titre}, Lien: {article.lien}\n")
        print("-" * 50)
else:
    print("Aucun article trouvé pour ces mots-clés.")

  

storage = Storage("data/resultats.json", format="json")
storage.sauvegarder(resultats)

          