# -*- coding: utf-8 -*-

"""
Definir uma dependência um para muitos entre objetos, de maneira que quando um objeto muda de estado todos os seus
dependentes são notificados e atualizados automaticamente. [1]

Abaixo vemos a classe Plataforma que estará agragada as classes computadores, então tudo que for alterdo na classe
Plataforma consequentimente o que foi declaro nas subclasses de Plataforma receberão notificações ou atuilização dessas
informações que pertecem a classe pai.

"""

class Plataforma():
    def __init__(self, nome, ano, fabricante):
        self.nome = nome
        self.ano = ano
        self.fabricante = fabricante

class Computador1():
    def __init__(self, marca, p):
        self.marca = marca
        self.p = p

    def informacoes(self):
        print self.marca + ' ' + self.p.nome + ' ' + self.p.ano + ' ' + self.p.fabricante


class Computador2():
    def __init__(self, marca, p):
        self.marca = marca
        self.p = p

    def informacoes(self):
        print self.marca + ' ' + self.p.nome + ' ' + self.p.ano + ' ' + self.p.fabricante

p = Plataforma("Linux", "1992", "Microsoft")
a = Computador1("Sansung", p)
b = Computador2("DELL", p)

a.informacoes()
b.informacoes()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""