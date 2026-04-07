import socket

PORTA = 10410 
HOST = '127.0.0.1'

def solicitar_acesso():
    print("--- ShadowGuard: Terminal de Acesso Remoto ---")
    senha = input("Digite a Credencial de Acesso: ")
    
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORTA))
        cliente.send(senha.encode('utf-8'))
        
        resultado = cliente.recv(1024).decode('utf-8')
        print(f"\n[SERVIDOR]: {resultado}")
        cliente.close()
    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    solicitar_acesso()