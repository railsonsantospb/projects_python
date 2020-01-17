# -*- coding: utf-8 -*-

"""
Garantir que uma classe tenha somente uma instância e fornece um ponto global de acesso para a mesma. [1]

No exemplo abaixo vemos como utulizar o padrão singleton, e podemos ver que sua função é justamente criar uma única inst-
ância do objeto carro, para que possa facilitar seu encapsulamento e também reutilização para as demais classes sem ter
que ficar instanciando objetos desta classe.
"""

class Carro:

    @staticmethod
    def getInstancia():
        c = Carro()
        if c == None:
            return Carro()
        return c

    def ano(self):
        print '2010'

    def motor(self):
        print '1.0v'

    def marca(self, p):
        print p.exibeInfo()

class FabricaCarros:
    def exibeInfo(self):
        pass

class Fiat(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Fiat"


class Volks(FabricaCarros):
    c = Carro()
    def __init__(self):
        self.f = self.c.getInstancia()

    def exibeInfo(self):
        return "Volks"

    def instanci(self):
        return self.f


class Chevrolet(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Chevrolet"


v = Volks()
v.instanci().marca(v)
v.instanci().ano()
v.instanci().motor()


"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""