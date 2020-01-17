# -*- coding: utf-8 -*-

"""
Fornecer uma interface unificada para um conjunto de interfaces em um subsistema. Facade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser usado. [1]

No exemplo abaixo vemos como representar várias funcionalidades atravéz de uma unica interface, economizando espaço de
e implementado um sistema OO, esse é o padrão facade, que tem por objetivo de representar um conjunto de operações
em uma única interface.
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