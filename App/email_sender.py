import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender():
    def __init__(self, remitente, passw, servidor_smtp, puerto_smtp):
        self.remitente = remitente
        self.passw = passw
        self.servidor_smtp = servidor_smtp
        self.puerto_smtp = puerto_smtp

    def enviar_correo(self, destinatario, asunto, mensaje):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.remitente
            msg['To'] = destinatario
            msg['Subject'] = asunto

            msg.attach(MIMEText(mensaje, 'plain'))

            smtp_obj = smtplib.SMTP(self.servidor_smtp, self.puerto_smtp)
            smtp_obj.starttls()

            smtp_obj.login(self.remitente, self.passw)

            smtp_obj.sendmail(self.remitente, destinatario, msg.as_string())

            print("Correo enviado con éxito")
        except smtplib.SMTPException as e:
            print(f"Error: No se pudo enviar el correo. {e}")
        finally:
            smtp_obj.quit()