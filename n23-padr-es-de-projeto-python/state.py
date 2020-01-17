# -*- codign: utf-8 -*-

"""
Permite a um objeto alterar seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe. [1]

Abaixo segue o exemplo de duas classes que possuim dois estados e possuiem dois métdos distintos, uma adciona e a outra
retira a vida de um personagem ou pessoa, a classe pessoa ela recebe um valor com a quantidade de vida que é determinado
pelo usuário, então quando agregamos o objeto pessoa com ambas as classes podemos adcionar e remover uma vida e assim
sucessitivamente alterando a parte interna do objeto.
"""

class Estado1():
    def __init__(self, objeto):
        self.objeto = objeto

    def valorDaVida(self):
        return self.objeto.vida

    def retirarVida(self):
        self.objeto.vida -= 1

class Estado2():
    def __init__(self, objeto):
        self.objeto = objeto

    def valorDaVida(self):
        return self.objeto.vida

    def adcionarVida(self):
        self.objeto.vida += 1

class Pessoa():
    def __init__(self, vida):
        self.vida = vida

p = Pessoa(10)
e = Estado1(p)
e.retirarVida()
e.retirarVida()
e = Estado2(p)
e.adcionarVida()
e = Estado1(p)
e.retirarVida()
print e.valorDaVida()

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""
