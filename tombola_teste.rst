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
    >>> t.carregar(bolas)
    >>> t.carregada()
    True

Deve ser possível sortear elementos de uma tômbola::
    >>> t.sortear()
    2
    >>> t.sortear()
    1
    >>> t.sortear()
    0
