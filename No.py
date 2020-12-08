from filme import Filme
from gerarFilme import printTree

class Node:
    def __init__(self, filme = None, left = None, right = None):
        self._filme = filme
        self._left = left
        self._right = right
        self._balance = 0
    
    def set_filme(self, filme):
        self._filme = filme

    def get_filme(self):
        return self._filme

    def set_left(self, left):
        self._left = left

    def get_left(self):
        return self._left

    def set_right(self, right):
        self._right = right

    def get_right(self):
        return self._right

    def insert(self, filme):
        if self.get_filme() == None:
            self.set_filme(filme)
            return self
        else:
            p = self
            while True:
                if p.get_filme().get_nome() > filme.get_nome():
                    if p.get_left() == None:
                        node = Node(filme)
                        p.set_left(node)
                        break
                    else:
                        p = p.get_left()
                elif p.get_filme().get_nome() < filme.get_nome():
                    if p.get_right() == None:
                        node = Node(filme)
                        p.set_right(node)
                        break
                    else:
                        p = p.get_right()
                elif p.get_filme().get_nome() == filme.get_nome():
                    print(f"O filme '{filme.get_nome()}' já foi inserido anteriormente.\nNão serão adicionados filmes homônimos.")
                    break
            
            if self.is_balanced(self) == False:
            	self = self.do_balance(self, filme.get_nome())
            return self
        
    def left_rotation(self, root):
        y = root.get_right()
        z = y.get_left()

        # Rotaciona
        y.set_left(root)
        root.set_right(z)

        # Muda os pesos
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root._balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y._balance = lh - rh

        # Retorna a raiz
        return y


    def right_rotation(self, root):
        y = root.get_left()
        z = y.get_right()

        # Rotaciona
        y.set_right(root)
        root.set_left(z)

        # Muda os pesos
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root._balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y._balance = lh - rh

        # Retorna a raiz
        return y

    def do_balance(self, root, key):
        balance = root._balance
        
        # Esquerda - Esquerda
        if balance > 1 and key < root.get_left().get_filme().get_nome():
            return self.right_rotation(root)

        # Direita - Direita
        if balance < -1 and key > root.get_right().get_filme().get_nome():
            y = self.left_rotation(root)
            return y
        
        # Rotação Dupla Esquerda - Direta
        if balance > 1 and key > root.get_left().get_filme().get_nome():
            root.set_left(root.left_rotation(root.get_left()))
            return self.right_rotation(root)

        # Rotação Dupla Direita - Esquerda
        if balance < -1 and key < root.get_right().get_filme().get_nome():
            root.set_right(root.right_rotation(root.get_right()))
            return self.left_rotation(root)

        return root
    
    ### PROCURAR POR ID
    def search_by_id(self, idFilme):  
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if left is not None:
                left.search_by_id(idFilme)
            if self.get_filme().get_idFilme() == idFilme:
                print(f"Nome: {self.get_filme().get_nome()}")
                print(f"Ano: {self.get_filme().get_ano()}")
                print(f"ID: {self.get_filme().get_idFilme()}")
            if right is not None:
                right.search_by_id(idFilme)
    
    ### LISTAR TODOS OS FILMES
    def list_items(self):
        right = self.get_right()
        left = self.get_left()
        if self is not None and self.get_filme() is not None:
            if left != None:
                left.list_items()
            print(f"Filme: {self.get_filme().get_nome()} - {self.get_filme().get_ano()} - ID: {self.get_filme().get_idFilme()}")
            if right != None:
                right.list_items()

    ### ALTURA
    def height(self, root):    
        if root is None:
            return 0
        return max(self.height(root.get_right()), self.height(root.get_left())) + 1

    ### CHECAR BALANCEAMENTO
    def is_balanced(self, root):
        if root is None:
            return True

        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root._balance = lh - rh

        if ((abs(lh - rh) <= 1) and self.is_balanced(root.get_left()) is True and self.is_balanced(root.get_right()) is True):
            return True

        return False
        
    ## IMPRIMIR ÁRVORE        
    def __str__(self, depth = 0):
        return str(printTree(self)).replace("None", '')