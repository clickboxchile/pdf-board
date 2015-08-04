import smtplib
from django.core.mail.utils import DNS_NAME
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class SSLEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = smtplib.SMTP_SSL(self.host, self.port,
                                               local_hostname=DNS_NAME.get_fqdn())
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silently:
                raise


def enviar_correo(txt_template, html_template, data_context, asunto, remitente, destinatario):
    plaintext = get_template(txt_template)
    htmly = get_template(html_template)
    d = Context(data_context)
    subject, from_email, to = asunto, remitente, destinatario
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=True)