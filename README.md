# Desafio DIO – Simulação de Ransomware e Keylogger (Ambiente Controlado)

Este projeto demonstra, **em ambiente 100% seguro**, a simulação didática de:
- Um *ransomware* simples em Python (criptografia + descriptografia).
- Um *keylogger* simples (captura de teclas e envio opcional por e‑mail).
- Medidas de defesa e prevenção.

## 📁 Estrutura do Repositório
```
├── scripts/
│   ├── ransomware.py
│   ├── decrypt.py
│   └── keylogger.py
├── images/
│   └── (capturas de tela – você adicionará)
└── README.md
```

## 🚨 Aviso
Este projeto é somente para fins **educacionais**, seguindo as diretrizes do curso.  
Não execute esses códigos em máquinas de terceiros.

## 🔐 Ransomware Simulado
O script `ransomware.py`:
- Gera uma chave Fernet.
- Criptografa arquivos de teste.
- Exibe mensagem de “resgate” simulada.

O script `decrypt.py`:
- Utiliza a chave para restaurar os arquivos originais.

## 🎧 Keylogger Simulado
O arquivo `keylogger.py`:
- Captura teclas pressionadas.
- Armazena em `log.txt`.
- Pode opcionalmente enviar o arquivo por e‑mail (comentado no código).

## 🛡 Defesa e Prevenção
- Uso de antivírus.
- Firewall configurado.
- Execução em sandbox/VM.
- Privilégios mínimos.
- Conscientização do usuário.
