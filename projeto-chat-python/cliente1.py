#-*-coding:utf-8-*-
import socket
from threading import Thread

class VerificaMensagens(Thread):
    def __init__(self, tcp):
        Thread.__init__(self)
        self.tcp_cliente_socket = tcp
    def run(self):
        self.tcp_cliente_socket= tcp
        self.fechar= False
        while (not self.fechar):
            data = self.tcp_cliente_socket.recv(1024)
            if (data):
                print data
        print "saiu do laco"
    def fecharVerificaMensagens(self):
        self.fechar = True
        self.tcp_cliente_socket.close()
        

#setar aqui o endereço IP do servidor
HOST, PORT = sys.argv[1], int(sys.argv[2])

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))


nome = raw_input( "Digite seu nome: ")
verificaMsg = VerificaMensagens(tcp)
verificaMsg.start()

print 10*'*'+"\nSEJA BEM VINDO\n" + 10*'*'+ '\n'

texto = ""
while texto != "sair":
    texto = raw_input("")
    tcp.send("\n"+nome+" : "+ texto)

verificaMsg.fecharVerificaMensagens()
print "finalizado"
