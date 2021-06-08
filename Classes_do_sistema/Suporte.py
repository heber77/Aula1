import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Suporte:
    def __init__(self):
        pass

    def enviarDuvida(self, duvida):
        # Criando um objeto mensagem
        msg = MIMEMultipart()

        mensagem = duvida

        # Configurando parâmetros da mensagem
        password = "adFv%Qrp"
        msg['From'] = "projetoclick1@gmail.com"
        msg['To'] = "projetoclick1@gmail.com"
        msg['Subject'] = "Subscription"

        # Adicionando o texto da mensagem
        msg.attach(MIMEText(mensagem, 'plain'))

        # Criar servidor
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login
        server.login(msg['From'], password)

        # Enviar a mensagem
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
        confir = "Sua dúvida foi enviada com sucesso"

        return confir