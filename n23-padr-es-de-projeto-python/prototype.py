# -*- coding: utf-8 -*-

"""
Especificar tipos de objetos a serem criados usando uma instância protótipo e criar novos objetos pela cópia desse
protótipo. [1]

O prototype não se diferencia muito dos outros opadrões explicado anterirormente, e temos que lembrar que o objetivo des-
ses padrões é criar objetos que possam auxiliar na manutenção e relação das classes com as subclasses, mas de certa forma
o prototype vem viabilizar e facilitar a copia do objeto realizando a reutilização e construção de outros objetos isso di-
ferenciando dos demais.
"""

class Carro:
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


class Volks(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Volks"

class Chevrolet(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Chevrolet"

class Prototype(Carro):
    def __init__(self, o):
        self.o = o

f = Fiat()
p = Prototype(f)
p.motor()
p.ano()
p.marca(f)
print
c = Chevrolet()
v = Volks()
v.marca(c)
v.ano()
v.motor()


"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""
