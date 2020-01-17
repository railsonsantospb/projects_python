# -*- coding: utf-8 -*-

"""
Converter a interface de uma classe em outra interface, esperada pelo cliente. O Adapter permite que interfaces
incompatíveis trabalhem em conjunto – o que, de outra forma, seria impossível. [1]

Vemos uma exemplo abaixo como se desenrrola o a interface da classe reprodutor nas subclasses mostrando a flexibilidade
de reutiliazação e adptação em outras classes subsequentes.

"""

class Reprodutor:

    def carregarImagem(self):
        pass

    def desenharImagem(self):
        pass

class Imagem(Reprodutor):
    __p = ''
    def carregarImagem(self, p):
        self.__p += '.'+p

    def desenharImagem(self, p):
        print p+self.__p

jpg = Imagem()
jpg.carregarImagem('jpg')
jpg.desenharImagem('Nuvem')

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""