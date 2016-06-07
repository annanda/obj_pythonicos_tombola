========================
Testes da classe Tombola
========================

Deve ser possível criar uma tômbola vazia::

    >>> from tombola import Tombola
    >>> t = Tombola()

Ao criar uma tômbola vazia, o método carregada deve retornar Falso
    >>> t.carregada()
    False

