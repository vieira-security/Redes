import socket
from datetime import datetime

PORTA = 10410 # 5 primeiros do seu TIA 
HOST = '127.0.0.1'
SENHA_MESTRA = "ShadowGuard-2026"

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(5)

print(f"[*] Sistema de Monitoramento ShadowGuard ativo na porta {PORTA}...")

while True:
    conn, addr = servidor.accept()
    log_entry = f"[{datetime.now()}] Conexao recebida de {addr}\n"
    
    # Recebe a tentativa de senha
    tentativa = conn.recv(1024).decode('utf-8')
    
    if tentativa == SENHA_MESTRA:
        resposta = "ACESSO CONCEDIDO. Bem-vindo, Administrador."
        status = "SUCESSO"
    else:
        resposta = "ACESSO NEGADO. Tentativa registrada."
        status = "FALHA/INTRUSAO"
    
    # Manipulação de Arquivo 
    with open("seguranca_audit.log", "a") as arquivo_log:
        arquivo_log.write(f"{log_entry} > Status: {status} | Input: {tentativa}\n")
        arquivo_log.write("-" * 50 + "\n")

    print(f"[!] Log gerado para {addr} - Status: {status}")
    conn.send(resposta.encode('utf-8'))
    conn.close()