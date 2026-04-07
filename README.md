# Redes
Laboratorio 3 - Analise Programação de Socket UDP e TCP

# Laboratório 03 - Redes de Computadores
## Programação de Sockets UDP/TCP e Monitoramento de Segurança

Este repositório contém as atividades práticas do Laboratório 03 da disciplina de Redes de Computadores (Mackenzie). [cite_start]O projeto explora as diferenças entre os protocolos da camada de transporte e apresenta uma aplicação prática voltada para cibersegurança. [cite: 1, 2, 3, 20]

---

## 📋 Conteúdo do Projeto

[cite_start]O laboratório foi dividido em três frentes principais de desenvolvimento e análise: [cite: 44, 57]

### 1. Análise de Protocolos (Questão 1)
Comparação prática entre **TCP** (orientado à conexão) e **UDP** (não orientado à conexão). 
* [cite_start]**TCP:** Demonstração de falha de conexão (`ConnectionRefusedError`) ao iniciar o cliente antes do servidor. [cite: 13]
* [cite_start]**UDP:** Demonstração de envio de datagramas sem a necessidade de um *handshake* prévio. [cite: 14, 15]

### 2. Chat Interativo (Questão 2)
[cite_start]Implementação de um chat bidirecional utilizando sockets. [cite: 17]
* [cite_start]**Porta utilizada:** 24000 (Baseada nos primeiros 5 dígitos do TIA). [cite: 18]
* [cite_start]**Controle:** Encerramento automático de ambas as pontas ao receber o comando `QUIT`. [cite: 17]

### 3. Desafio: AuraGuard Log Monitor (Questão 3)
[cite_start]Aplicação inspirada no projeto de TCC **AuraGuard**, focada em segurança defensiva. [cite: 30, 50]
* [cite_start]**Função:** Atua como um *HoneyPot* de autenticação que monitora tentativas de acesso remoto. [cite: 30]
* [cite_start]**Manipulação de Arquivos:** O servidor gera e atualiza dinamicamente um arquivo de log (`seguranca_audit.log`) contendo IP, Data, Hora e o status da tentativa de acesso. [cite: 32, 33, 35]

---

## 🚀 Como Executar

### Pré-requisitos
* [cite_start]Python 3.10 ou superior. 

### Executando o Monitor de Segurança (Questão 3)

1. **Inicie o Servidor:**
   ```bash
   python HoneyPot_Server.py
