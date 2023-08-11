from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from charityapp.user_accounts.models import AppUser


@receiver(pre_save, sender=User)
def set_user_type(sender, instance, **kwargs):
    if instance.is_superuser and not hasattr(instance, 'appuser'):
        AppUser.objects.create(user=instance, user_type='MEMBER')
