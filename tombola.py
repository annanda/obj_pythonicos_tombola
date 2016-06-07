class Tombola:
    bolas = None

    def carregada(self):
        return bool(self.bolas)

    def carregar(self, lista):
        self.bolas = lista
