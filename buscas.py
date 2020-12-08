def buscaAno(self, year):
    vetor = []
    return anoList(self, vetor, year)

def anoList(self, vetor, year):
    if self != None:
        anoList(self._left, vetor, year)
        if self.get_filme().get_ano() == year:
            vetor.append(f'Título: {self.get_filme().get_nome()} - ID: {self.get_filme().get_idFilme()}')            
        anoList(self._right, vetor, year)
        return vetor


