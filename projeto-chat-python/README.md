# README #

Segue um exemplo de como utilizar Sockets e Threads com dois clientes e um servidor. A diferença para algumas aplicações simples feitas em python é que nesse exemplo que foi desenvolvido você no caso o cliente, recebe mensagens de todos os outros clientes que estejam conectado ao mesmo servidor que sua aplicação, e assim vale para todos os outros clientes. Essa estrutura é um exemplo de uma rede multcast, na qual só está recebendo as mensagens daquele grupo de usuários que estão conectados aquele servidor. 

Para iniciar o server.py você abre o terminal ou prompt de comando, vai até na pasta onde está o arquivo mensionado e digita: python server.py "ip-da-maquina" "porta"

Já nos arquivos clientes, quando for abrir em outra máquina, você deve ir no diretório no qual ele está localizado e digitar: python cliente1.py "ip-do-servidor" "porta-do-servidor". Dessa forma poderemos se conectar com o servidor e realizar a comunicação com outros clientes que estão conectados naquele mesmo endereço em uma rede local onde as máquinas conseguem se enchergar.