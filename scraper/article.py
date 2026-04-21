class Article:
    """Représente un article de presse collecté."""

    def __init__(self,titre,lien,source):
        self.titre = titre
        self.lien = lien
        self.source = source

        def __str__(self):
            return f"[{self.source}] {self.titre}\n{self.lien}"