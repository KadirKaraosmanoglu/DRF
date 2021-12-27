from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(receiver=create_auth_token, sender=get_user_model())
