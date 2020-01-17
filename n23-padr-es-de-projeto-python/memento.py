# -*- coding: utf-8 -*-

"""
Sem violar o encapsulamento, capturar e externalizar um estado interno de um objeto, de maneira que o objeto possa ser
restaurado para esse estado mais tarde.” [1]

Abaixo segue um exemplo um editor de texto, na classe texto você escreve e salva o texto dentro de uma lista, assim
na proxima recuperação de alguma linha que foi apagada recentimento apagará a linha mais antiga, e é na classe caretaker
onde esttá salva na lista, dessa forma não haverá um armazenamento de informações descontrolada.mantendo o estado
interno do objeto mesmo podendo externalizar suas informções.


"""

class Texto():

    def __init__(self, texto):
       self.texto = texto

    def salvarTexto(self):
        return self.texto


class CareTake():
    __save = []
    def __init__(self, texto):
        self.texto = texto
        self.__save.append(texto)

    def escreverTexto(self):
        return [i for i in self.__save]

    def desfazerTextoAntigo(self):
        try:
            self.__save.pop(0)
        except IndexError:
            print 'editor vázio'

t = Texto('Olá bom dia!')
c = CareTake(t.salvarTexto())
t = Texto('Olá boa tarde!')
c = CareTake(t.salvarTexto())
t = Texto('Olá boa noite!!')
c = CareTake(t.salvarTexto())
t = Texto('Olá boa madrugada!')
c = CareTake(t.salvarTexto())
print c.escreverTexto()
c.desfazerTextoAntigo()
print c.escreverTexto()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""