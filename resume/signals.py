from django.core.mail import send_mail
from django.conf import settings



def send_welcomeMail(subject,message,recipient,**kwargs):

    send_mail(subject,
              message,
              settings.EMAIL_HOST_USER,
              [recipient],
              fail_silently=False,
              )