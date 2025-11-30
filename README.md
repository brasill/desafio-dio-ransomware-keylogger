# 🛡️ Desafio de Cibersegurança: Malware Simulation

Projeto desenvolvido para o Bootcamp da DIO. O objetivo foi implementar um Ransomware e um Keylogger em Python para entender o funcionamento dessas ameaças e como se proteger.

## 💻 Ambiente de Desenvolvimento
Este projeto foi adaptado para rodar em **Linux (Gentoo)**, exigindo configurações específicas de ambiente e permissões diferentes do Windows.

- **Sistema Operacional:** Gentoo Linux
- **Linguagem:** Python 3.13
- **Bibliotecas:** `pynput`, `cryptography`

## 📁 Estrutura do Projeto
- `/ransomware`: Scripts de criptografia (AES) e descriptografia de arquivos.
- `/keylogger`: Script de captura de teclas com suporte a envio de e-mail e execução em background.

## 🔧 Desafios e Soluções (Learning Outcomes)
1. **Ambiente Virtual (PEP 668):** Utilização de `venv` para isolar dependências do sistema (`emerge`).
2. **Servidor Gráfico:** Configurações específicas para captura de input no X11.
3. **Furtividade:** Execução em background via `nohup` para simular processo daemon.

## 🛡️ Prevenção e Defesa
- **Ransomware:** Backups imutáveis e princípio do privilégio mínimo.
- **Keylogger:** Uso de MFA (Autenticação de Dois Fatores) e EDRs comportamentais.

---
*Este projeto é puramente educacional.*
