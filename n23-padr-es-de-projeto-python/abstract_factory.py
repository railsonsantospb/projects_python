# -*- coding: utf-8 -*-

"""
Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. [1]

Abaixo reutilizamos o código do exemplo anterior, implementando só mais uma classe para representar um devido grupo de
carros de um específico ano.Esse é o padrão abstract method
"""


class FabricaCarros:
    def exibeInfo(self):
        pass

class Fiat(FabricaCarros):

    def exibeInfo(self):
        return "Fiat"


class Volks(FabricaCarros):

    def exibeInfo(self):
        return "Volks"

class Chevrolet(FabricaCarros):

    def exibeInfo(self):
        return "Chevrolet"

class Carro2010:
    __carro = {}
    def __init__(self, p):
        self.__carro['2010'] = p.exibeInfo()

    def carro(self):
        print self.__carro

c = Chevrolet()
v = Volks()
n = Carro2010(c)
n.carro()
n = Carro2010(v)
n.carro()


"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""