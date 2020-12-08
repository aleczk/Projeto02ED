from filme import Filme
from No import Node
from gerarFilme import create_movie_and_insert
from buscas import buscaAno, anoList

def menu():
    print("__"*20)
    print("(1) Inserir um Filme")    
    print("(2) Buscar Filme pelo ID")
    print("(3) Buscar Filmes pelo Ano")
    print("(4) Listar Filmes em Ordem Alfabética")
    print("(5) Altura da Árvore")
    print("(6) Exibir Árvore")
    print("(7) Sair")
    print("‾‾"*20)
    escolha = int(input("Option: "))
    print()
    return escolha

def main():
    root = Node()
    escolha = menu()
    while escolha != 7:
        
        if escolha == 1:
            root = create_movie_and_insert(root)
        
        elif escolha == 2:
            try:
                ano = int(input("ID: "))
                root.search_by_id(ano)
            except ValueError:
                print("ID inválido, digite números, não strings.")
            except AttributeError:
                print("ID não encontrado.")
        
        elif escolha == 3:
            ano = int(input("Ano do Filme: "))
            buscar = buscaAno(root, ano)
            if buscar == [] or buscar == None:
                print("Filme não encontrado.")
            else:
                print(f"\nFilmes Encontrados no ano de {ano}:")
                print(*buscar, sep="\n")
                
        elif escolha == 4:
            print("Lista de todas os Filmes Alfabeticamente: ")
            root.list_items()
            
        elif escolha == 5:
            print(f"Altura da arvore: {root.height(root) - 1}")
 
        elif escolha == 6:
            print(root)
        
        else:
            print("Escolha inválida.")
        escolha = menu()
        
if __name__ == "__main__":
    main()

