# -*- coding: utf-8 -*-

"""
Definir o esqueleto de um algoritmo em uma operação, postergando alguns passos para as subclasses. Template Method
permite que subclasses redefinam certos passo de um algoritmo sem mudar a estrutura do mesmo. [1]

Abaixo vemos um exemplo de uma lista de tuplas que possui dados pertinentes aos alunos, para facilitar a ordenação por
nome, idade ou série, criamos uma classe que ao receber essa lista e o indece no qual irá representar a forma por qual
atributo do aluno ordenará essa lista.

"""

class Ordenar(object):
    __saida = ''
    def __init__(self, tipo, estudante):
        self.tipo = tipo
        self.estudante = estudante

    def ordenaTipo(self):

        if self.tipo == 0:
            self.__saida = sorted(self.estudante, key=lambda student: student[0])   # Ordena pelo nome
        if self.tipo == 1:
            self.__saida = sorted(self.estudante, key=lambda student: student[1])   # Ordene pela serie
        if self.tipo == 2:
            self.__saida = sorted(self.estudante, key=lambda student: student[2])   # Ordena pela idade

    def escreve(self):
        print self.__saida

estudante = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

o = Ordenar(2, estudante)
o.ordenaTipo()
o.escreve()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""