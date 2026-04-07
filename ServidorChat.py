import socket

# Primeiros 5 números do seu TIA 
PORTA = 10410
HOST = '127.0.0.1'

# Criando o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(1)

print(f"Aguardando conexão na porta {PORTA}...")
conexao, endereco = servidor.accept()
print(f"Conectado com: {endereco}")

while True:
    # Recebe a mensagem do cliente
    mensagem_recebida = conexao.recv(1024).decode('utf-8')
    
    #Verificar se é comando QUIT
    if mensagem_recebida.upper() == "QUIT":
        print("O cliente encerrou o chat.")
        break
        
    print(f"Cliente diz: {mensagem_recebida}")
    
    # Envia a resposta
    resposta = input("Sua resposta (ou QUIT para sair): ")
    conexao.send(resposta.encode('utf-8'))
    
    if resposta.upper() == "QUIT":
        break

conexao.close()
servidor.close()