# -*- condign: utf-8 -*-

"""
Evitar o acoplamento do remetente de uma solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de
tratar a solicitação. Encadear os objetos receptores, passando a solicitação ao longo da cadeia até que um objeto a
trate. [1]

Segue abaixo um exemplo que mostra uma classe banco que podemos criar vários bancos dentro dela, então de acordo
inserimos um nome vamos criando um banco, e em seguida quando vamos depositar procuramos especificar pelo nome do banco
no qual tratará de receber um específico valor.

"""

class Banco():
    __r = {}
    def __init__(self, nome):
        self.__r[nome] = ''

    def sacar(self, nome, valor):
        self.__r[nome] = valor

    def depositar(self, nome, valor):
        self.__r[nome] = valor

    def bancos(self):
        for i in self.__r.keys():
            print i, self.__r[i]

b = Banco('Brasil')
b = Banco('Bradesco')
b.depositar('Brasil', '100.00')
b.depositar('Bradesco', '300.00')
b.bancos()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""