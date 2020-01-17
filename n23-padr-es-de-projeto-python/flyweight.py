# -*- coding: utf-8 -*-

"""
Usar compartilhamento para suportar eficientemente grandes quantidades de objetos de granularidade fina. [1]

Bom, abaixo foiutulizado o mesmo esxemplo do padrão facade, pois o objetivo do padrão flyweight é quase o mesmo, no qual
cria uma interface ou objeto para suportar o compartilhamento de um conjunto de outros objetos.
"""

class Video:

    def __init__(self):
        pass

    def carregarImagem(self, imagem):
        print 'Imagem "{}" Carregada!'.format(imagem)

class Audio:

    def __init__(self):
        pass

    def carrgarAudio(self, audio):
        print 'Audio "{}" Carregado!'.format(audio)


class Sistema:

    def __init__(self):
       self.__au = Audio()
       self.__v = Video()

    def carregarSistema(self):
        return self.__au, self.__v

s = Sistema()
a, v = s.carregarSistema()
a.carrgarAudio("teste.mp3")
v.carregarImagem("teste.mkv")

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""