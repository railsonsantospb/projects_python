# -*- coding: utf-8 -*-

"""
Compor objetos em estruturas de árvore para representar hierarquia partes-todo. Composite permite aos clientes tratarem
de maneira uniforme objetos individuais e composições de objetos. [1]

Segue abaixo um exemplo de um gerenciador de arquivos, onde criamos uma paste e em seguida geramos e copiamos arquivos
para a pasta que foi criada, essa forma estrutural identifica como deve ser utilizado o padrão composite.
"""

class Servidor:

    def remover(self):
        pass

    def inserir(self):
        pass

    def copiar(self):
        pass

class Arquivo(Servidor):

    def __init__(self, nome):
        self.nome = nome

    def gerar(self):
        return self.nome

    def inserir(self):
        return self.nome

    def remover(self):
        del self.nome

    def copiar(self):
        return self.nome+'(copy)'

class Pasta(Servidor):

    __store = {}
    __s = []
    def __init__(self, nome):
        self.nome = nome


    def guardar(self, data):

        self.__s.append(data)
        self.__store[self.nome] = self.__s

    def listar(self):
        for i in self.__store.keys():
            print i+'/',
            print self.__store[i]

if __name__ == '__main__':
    p1 = Pasta('Images')

    a1 = Arquivo('teste1.jpg')
    a2 = Arquivo('teste2.jpg')
    a3 = Arquivo('teste1.jpg')

    p1.guardar(a1.gerar())
    p1.guardar(a2.gerar())
    p1.guardar(a3.copiar())

    p1.listar()



"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""