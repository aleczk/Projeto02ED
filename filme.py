class Filme:
    def __init__(self, nome=None, ano=None, idFilme=None):
        self._nome = nome
        self._idFilme = idFilme
        self._ano = ano

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_idFilme(self, idFilme):
        self._idFilme = idFilme

    def get_idFilme(self):
        return self._idFilme

    def set_ano(self, ano):
        self._ano = ano

    def get_ano(self):
        return self._ano