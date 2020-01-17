# -*- coding: utf-8 -*-

"""
Dada uma linguagem, definir uma representação para sua gramática juntamente com um interpretador que usa a representação
para interpretar sentenças dessa linguagem. [1]

Abaixo segue uma classe chamda numeroperfeito que será responsável de identificar se o número que for passado pelo método
construtor da classe é perfeito ou não, o intuito dessa classe ou algoritmo é mostrar a como posso inserir novos formas
gramáticais para verificar o número ou números, um exmplo do que poderiamos fazer é além de identificar se o número
é perfeito podemos inserir uma grámatica ou funcionalidade no mesmo algoritmo para verificar se o número é primo ou não
sem perder sua integridade anterior. Esse padrão é muito parecido com o Template Method

"""


class NumeroPerfeito():
    def __init__(self, numero):
        self.numero = numero

    def analisar(self):
        l = []
        v = 0
        for i in xrange(1, self.numero):
            if self.numero % i == 0:
                l.append(i)
        for i in l:
            v += i

        return v == self.numero

n = NumeroPerfeito(6)
print n.analisar()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""
