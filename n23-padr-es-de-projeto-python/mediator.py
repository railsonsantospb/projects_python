# -*- coding: utf-8 -*-


"""
Definir um objeto que encapsula a forma como um conjunto de objetos interage. O Mediator promove o acoplamento fraco
ao evitar que os objetos se refiram uns aos outros explicitamente e permitir variar suas interações independentemente. [1]

Abaixo vemos um exemplo de comunicação, quando o sistema android envia uma mensagem para o ios eles precisam passar por
um mediador, pois é inviavel se comunicar diretamante, principalmente por possuirem protocolos de comunicação diferente
nesse caso, então criamos a classe menssage que será interceptar a mensagem e será responsável de enviar uma mensagem
para um o aparelho que passamos no argumento do método da classe.

"""


class Android():
    def __init__(self, m):
        self.m = m

    def enviar_mensagem(self):
        return self.m

    def receber_mensagem(self, r):
        return r


class IOS():
    def __init__(self, m):
        self.m = m

    def enviar_mensagem(self):
        return self.m

    def receber_mensagem(self, r):
        return r

class Sybiam():
    def __init__(self, m):
        self.m = m

    def enviar_mensagem(self):
        return self.m

    def receber_mensagem(self, r):
        return r

class Menssage():
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def chat(self):
        print self.c2.receber_mensagem(self.c1.enviar_mensagem())

a = Android("Olá sou Android")
i = IOS("Olá sou IOS")

m = Menssage(i, a)

m.chat()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""