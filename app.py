from flask import Flask, render_template, request
from scraper.aggregator import Aggregator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultats = []
    mots_cles = ""

    if request.method == "POST":
        mots_cles = request.form.get("mots_cles", "")
        mots_liste = [mot.strip() for mot in mots_cles.split(",")]

        agg = Aggregator(mots_liste)
        agg.ajouter_source("BBC News", "https://feeds.bbci.co.uk/news/rss.xml")
        agg.ajouter_source("France 24", "https://www.france24.com/fr/rss")
        agg.collecter_tous()
        resultats = agg.filtrer()

    return render_template("index.html", resultats=resultats, mots_cles=mots_cles)

if __name__ == "__main__":
    app.run(debug=True)