# -*- coding: utf-8 -*-

"""
“Definir uma interface para criar um objeto, mas deixar as subclasses decidirem que classe instanciar. O Factory Method
permite adiar a instanciação para subclasses. [1]

Segue abaixo um exemplo de como utilizar o factory method, e também vemos um grande exemplo de emcapsulamento do objeto,
tornando sua criação ou instânciação responsável para outras subclasses.
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

c = Chevrolet()
c = Volks()
print c.exibeInfo()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""