# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
#
# UserModel = get_user_model()
#
#
# def send_successful_registration_email(user):
#     html_message = render_to_string(
#         'emails/email-greeting.html',
#         {'user': user},
#     )
#
#     plain_message = strip_tags(html_message)
#
#     send_mail(
#         subject='Registration successful!',
#         message=plain_message,
#         html_message=html_message,
#         from_email=settings.EMAIL_HOST_USER,
#         # CHECK WHETHER YOUR USER HAVE EMAIL FIELD
#         recipient_list=(user.email,)
#     )
#
#
# @receiver(post_save, sender=UserModel)
# def user_created(instance, created, **kwargs):
#     if created:
#         send_successful_registration_email(instance)

from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from charityapp.user_accounts.models import AppUser


@receiver(pre_save, sender=User)
def set_user_type(sender, instance, **kwargs):
    if instance.is_superuser and not hasattr(instance, 'appuser'):
        AppUser.objects.create(user=instance, user_type='MEMBER')
