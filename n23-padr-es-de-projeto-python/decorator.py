# -*- coding: utf-8 -*-

"""
Dinamicamente, agregar responsabilidades adicionais a objetos. Os Decorators fornecem uma alternativa flexível ao uso
de subclasses para extensão de funcionalidades. [1]

O exemplo abaixo mostra como o padrão decorator pode ajudar a utilizar de forma dinâmica a classe coquitel em outras
classes, isso sempre seguindo o objetivo do problema.
"""

class Coquitel:

    def __init__(self, tipo):
        self.tipo = tipo

    def nomeC(self):
        print self.tipo.nome

    def precoC(self):
        print self.tipo.preco


class Cachaca:
    nome = 'Cachaca'
    preco = 10.0


class Vodk:
    pass
    '''
        Aqui você também pode seguir a mesma lógica, bem simples e direta.
    '''

c = Coquitel(Cachaca)
c.nomeC()
c.precoC()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""