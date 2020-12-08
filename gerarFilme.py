from filme import Filme

ids = 0

def create_movie_and_insert(root):
    nome = input("Nome do Filme: ")
    global ids 
    ids += 1
    try:
        ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("\nErro. Digite números, não strings.\n")
        ano = int(input("Ano de lançamento: "))
    print(f'\n{nome} - {ano} - ID: {ids} inserido com sucesso.\n')
    filme = Filme(nome, ano, ids)
    root = root.insert(filme)
    return root

def printTree(self, depth = 0):
    if self != None:
        printTree(self._left, depth + 1)
        print(' ' * 4 * depth + '->', self._filme._idFilme)
        printTree(self._right, depth + 1)