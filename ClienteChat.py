import socket

#Mesma porta do servidor (5 primeiros do TIA)
PORTA = 10410
HOST = '127.0.0.1'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))

print("Chat iniciado! Digite QUIT para encerrar.")

while True:
    mensagem = input("Sua mensagem: ")
    cliente.send(mensagem.encode('utf-8'))
    
    #Verificar se é comando QUIT
    if mensagem.upper() == "QUIT":
        break
        
    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode('utf-8')
    
    if resposta.upper() == "QUIT":
        print("O servidor encerrou o chat.")
        break
        
    print(f"Servidor diz: {resposta}")

cliente.close()