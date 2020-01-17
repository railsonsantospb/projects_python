# -*- coding: utf-8 -*-


"""
Separar a construção de um objeto complexo de sua representação de modo que o mesmo processo de construção possa criar
diferentes representações. [1]

O exemplo abaixo é parecido com os outros dois padrões anteriores, o factory_method e abstract_method, a única coisa que
vai deiferencia-lo dos demais é que irá separar as operaçãoes dos objetos facilitando na implementação de novas operções
com outras interfaces que desejam operar.
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

class Fiat(FabricaCarros):

    def exibeInfo(self):
        return "Fiat"


class Volks(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Volks"

class Chevrolet(FabricaCarros, Carro):

    def exibeInfo(self):
        return "Chevrolet"

c = Chevrolet()
v = Volks()
v.marca(c)
v.ano()
v.motor()


"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""