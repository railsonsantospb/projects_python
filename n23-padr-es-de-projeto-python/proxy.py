# -*- coding: utf-8 -*-

"""
Fornecer um substituto ou marcador da localização de outro objeto para controlar o acesso a esse objeto. [1]

Abaixo vemos que esse padrão tem como objetivo de implementar outro objeto para que possa se responsabilizar pela segu-
rança do outro objeto no qual é nosso objetivo acessar, então o proxy providencia uma implementação intermediária para
filtrar o acesso em um determinado objeto.
"""

class Banco:
    __users = {}
    __users['1'] = 'Madara'
    __users['2'] = 'Tobi'
    __users['3'] = 'Deidara'
    def usuarioID(self):
        for i in self.__users.keys():
            print self.__users[i]

class Acesso:
    b = Banco()
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def acessarContas(self):
        if self.login and self.senha:
            self.b.usuarioID()
        else:
            print "NULL"

a = Acesso("madara", "123")
a.acessarContas()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""