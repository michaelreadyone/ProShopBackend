'''
Manipulate Django signals to sync the username and email( instead of overwriting the Django user model, try outside fix. Also we don't want to touch the django original content because an version update may triger some mistakes )
Introduction to django signal
https://www.youtube.com/watch?v=Kc1Q_ayAeQk
'''

from django.db.models.signals import pre_save
from django.contrib.auth.models import User


def updateUser(sender, instance, **kwargs):
    print('Signal Trigged')
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)
