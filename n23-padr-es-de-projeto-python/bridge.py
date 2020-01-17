# -*- coding: utf-8 -*-


"""
Desacoplar uma abstração da sua implementação, de modo que as duas possam variar independentemente. [1]

"""

class Janelas:

    def __desenharJanela(self):
        pass

    def __desenharBotao(self):
        pass

    def desenhar(self):
        pass

class JanelaDialogo(Janelas):

    def __init__(self, plataforma):
        self.plataforma = plataforma

    def __desenharJanela(self):
        print self.plataforma.nome(),
        print ' Dialogo'

    def __desenharBotao(self):
        print self.plataforma.nome(),
        print ' Botao'

    def desenhar(self):
        self.__desenharJanela()
        self.__desenharBotao()

class JanelaAviso(Janelas):
    pass
    '''
        Aqui pode ser implementado a mesma lógica de cima, claro, mudando o que é óbivo para que fique explicito cada
        necessidade.
    '''

class JanelaLinux:

    def nome(self):
        return 'Linux'

l = JanelaLinux()
d = JanelaDialogo(l)
d.desenhar()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""
