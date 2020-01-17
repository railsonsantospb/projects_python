# -*- encoding:utf-8 -*-
from __future__ import print_function

"""
Representar uma operação a ser executada nos elementos de uma estrutura de objetos. Visitor permite definir uma nova
operação sem mudar as classes dos elementos sobre os quais opera. [1]

Segue abaixo um exemplo utulizando um algoritmo básico de árvore binária, inseridno e percorrendo sua estrutura, para isso
contruimos algortimos sem perder a integridade do outros que estão sendo impostos sobre o mesmo objeto.
"""


class BSTNode(object):
    l = []
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def add(self, key):
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)

    def escreve(self, root):
        root(self.key)
        self.l.append(self.key)
        if self.left is not None:
            self.left.escreve(root)
        if self.right is not None:
            self.right.escreve(root)

    def print(self):
        self.escreve(print)

root = BSTNode(10)
root.add(4)
root.add(8)
root.print()
print(root.l)


"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""