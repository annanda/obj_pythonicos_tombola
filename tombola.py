class Tombola:
    bolas = None

    def carregada(self):
        return bool(self.bolas)

    def carregar(self, lista):

        # para que ele faca uma copia da lista recebida e nao use o mesmo objeto, alterando ele
        self.bolas = list(lista)

    def sortear(self):
        return self.bolas.pop()

    def misturar(self):
        pass