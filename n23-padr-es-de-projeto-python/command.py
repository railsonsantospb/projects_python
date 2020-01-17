# -*- coding: utf-8 -*-

"""
Encapsular uma solicitação como objeto, desta forma permitindo parametrizar cliente com diferentes solicitações,
enfileirar ou fazer o registro de solicitações e suportar operações que podem ser desfeitas. [1]

Criamos uma classe chamada compra, assim para realizar uma compra com o tipo de pagamento foi preciso criar objetos que
solicitasse uma operação para confirmar na compra que forma foi relaizada o pagamento atraves de parametrização.

"""

class Compra():
    def __init__(self, formaPagamento):
        self.formaPagamaneto = formaPagamento

    def pagamento(self):
        return self.formaPagamaneto.conta

class CartaoCredito():
    def __init__(self):
        self.__nome = "Cartão de Crédito"

    def pagar(self):
        return self.__nome

class CartaoDebito():
    def __init__(self):
        self.__nome = "Cartão de Débito"

    def pagar(self):
        return self.__nome

class Boleto():
    def __init__(self):
        self.__nome = "Boleto"

    def pagar(self):
        return self.__nome

cr = CartaoCredito()
cd = CartaoDebito()
b = Boleto()

c1 = Compra(b.pagar())
c2 = Compra(cr.pagar())
c3 = Compra(cd.pagar())

print c1.formaPagamaneto
print c2.formaPagamaneto
print c3.formaPagamaneto

"""

[1]  GAMMA, Erich et al. Padrões de Projeto: Soluções reutilizáveis de software orientado a objetos.

"""