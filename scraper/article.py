class Article:
   

    def __init__(self,titre,lien,source, resume=""):
        self.titre = titre
        self.lien = lien
        self.source = source
        self.resume = resume

    def __repr__(self):
        return f"Source: {self.source}, Titre: {self.titre}, Lien: {self.lien}, Résumé: {self.resume}\n"