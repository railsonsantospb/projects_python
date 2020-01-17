# -*- coding: utf-8 -*-

"""
Fornecer um meio de acessar, sequencialmente, os elementos de um objeto agregado sem expor sua representação subjacente [1]

Abaixo vemos ums exemplo de armazenar os nomes de canais utilizando uma lista emcapsulada dentro de uma classe, dessa forma
invocaremos a classe com seus respectivos métodos especiais para armazenar de forma sequencial as informações pertinentes para
poder acessalas..

"""


class AdcionarCanal(object):
    __adcionar = []

    def __init__(self, canal):
        self.canal = canal

    def add(self):
        self.__adcionar.append(self.canal)

    def __getitem__(self, item):
        return self.__adcionar[item]

a = AdcionarCanal("SBT")
a.add()
a = AdcionarCanal("GLOBO")
a.add()

for i in a:
    print i

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""