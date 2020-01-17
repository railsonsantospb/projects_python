# -*- coding: utf-8 -*-

"""
Definir uma família de algoritmos, encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam [1]

No exemplo abaixo vamos ver duas forma de utilizar a função sorted(), onde veremos nas classes
responsável de encapsular e tratar cada algoritmo e suas relações.

"""

class ClasseA(object):

    # Aqui realizamos uma ordenação crescente.
    def executeOrdenacao(self, lista):
        return sorted(lista)

class ClasseB(object):

    # Aqui realizamos uma ordenação decrescente.
    def executeOrdenacao(self, lista):
        return sorted(lista, reverse=True)


if __name__ == "__main__":

    l = [1,22,3,45,64]
    o = ClasseA()
    r = ClasseB()

    print o.executeOrdenacao(l)
    print r.executeOrdenacao(l)

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""


