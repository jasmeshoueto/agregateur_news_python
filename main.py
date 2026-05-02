from scraper.aggregator import Aggregator
from scraper.storage import Storage

print("===Agrégateur de News Personnalisé ====\n")

# 1. Saisie des mots-clés
mots_cles = input("Entrez vos mots-clés  (séparés par des virgules) : ")
mots_cles = [mot.strip() for mot in mots_cles.split(",") ]

# 2. Création de l'agrégateur
aggregator = Aggregator(mots_cles)

# 3. Ajout des sources
aggregator.ajouter_source("France 24", "https://www.france24.com/fr/rss")
aggregator.ajouter_source("BBC News", "https://feeds.bbci.co.uk/news/rss.xml")
aggregator.ajouter_source("RFI Afrique", "https://www.rfi.fr/fr/afrique/rss")



# 4. Collecte des articles
print("\nCollecte des articles...")
aggregator.collecter_tous()

# 5. Filtrage
resultats = aggregator.filtrer()

# Charger les anciens articles sauvegardés
storage = Storage("data/resultats.json", format="json")
anciens = storage.charger_json()

# Filtrer aussi les anciens
agg_anciens = Aggregator(mots_cles)
agg_anciens.articles = anciens
anciens_filtres = agg_anciens.filtrer()

# Combiner nouveaux et anciens
tous = resultats + [a for a in anciens_filtres if a.lien not in [r.lien for r in resultats]]

# Afficher
for article in tous:
    print(f"[{article.source}] {article.titre}")
    print(f"Lien : {article.lien}")
    print(f"Résumé : {article.resume}\n")
    print("-" * 50)



# 6. Affichage
if resultats:
    print(f"{len(resultats)} article(s) trouvé(s):\n")
    for article in resultats :
        print(f"Source: {article.source}, Titre: {article.titre}, Lien: {article.lien}, Resume: {article.resume}\n")
        print("-" * 50)
else:
    print("Aucun article trouvé pour ces mots-clés.")

  
# 7. Sauvegarde
storage = Storage("data/resultats.json", format="json")
storage.sauvegarder(resultats)

          