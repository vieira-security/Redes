# Redes
Laboratorio 3 - Analise Programação de Socket UDP e TCP

# Integrantes do Grupo
 Gabriel Vieira de Sousa /
 Guilherme Rainho Geraldo /
 Guilherme Gomes Arantes Teles

# Laboratório 03 - Redes de Computadores
## Programação de Sockets UDP/TCP e Monitoramento de Segurança

Este repositório contém as atividades práticas do Laboratório 03 da disciplina de Redes de Computadores (Mackenzie). O projeto explora as diferenças entre os protocolos da camada de transporte e apresenta uma aplicação prática voltada para cibersegurança. 

---

## 📋 Conteúdo do Projeto

O laboratório foi dividido em três frentes principais de desenvolvimento e análise:

### 1. Análise de Protocolos (Questão 1)
Comparação prática entre **TCP** (orientado à conexão) e **UDP** (não orientado à conexão). 
* **TCP:** Demonstração de falha de conexão (`ConnectionRefusedError`) ao iniciar o cliente antes do servidor. 
* **UDP:** Demonstração de envio de datagramas sem a necessidade de um *handshake* prévio. 

### 2. Chat Interativo (Questão 2)
Implementação de um chat bidirecional utilizando sockets. 
* **Porta utilizada:** 24000 (Baseada nos primeiros 5 dígitos do TIA). 
* **Controle:** Encerramento automático de ambas as pontas ao receber o comando `QUIT`. 
Link do Video: https://youtu.be/IqexY04xJy8

### 3. Desafio: AuraGuard Log Monitor (Questão 3)
]Aplicação inspirada no projeto de TCC **ShadowGuard**, focada em segurança defensiva. 
* **Função:** Atua como um *HoneyPot* de autenticação que monitora tentativas de acesso remoto. 
* **Manipulação de Arquivos:** O servidor gera e atualiza dinamicamente um arquivo de log (`seguranca_audit.log`) contendo IP, Data, Hora e o status da tentativa de acesso. 

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.10 ou superior. 

### Executando o Monitor de Segurança (Questão 3)

1. **Inicie o Servidor:**
   ```bash
   python HoneyPot_Server.py
