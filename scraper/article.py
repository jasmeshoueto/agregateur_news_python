class Article:
   

    def __init__(self,titre,lien,source):
        self.titre = titre
        self.lien = lien
        self.source = source

        def __repr__(self):
            return f"Source: {self.source}, Titre: {self.titre}, Lien: {self.lien}\n"