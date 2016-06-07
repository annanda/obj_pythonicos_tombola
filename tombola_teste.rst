========================
Testes da classe Tombola
========================

Deve ser possível criar uma tômbola vazia::

    >>> from tombola import Tombola
    >>> t = Tombola()

Ao criar uma tômbola vazia, o método carregada deve retornar Falso::

    >>> t.carregada()
    False

Deve ser possível carregar a tômbola com itens de uma lista::

    >>> bolas = list(range(3))
    >>> t.carregar()
    >>> t.carregada()
    True


