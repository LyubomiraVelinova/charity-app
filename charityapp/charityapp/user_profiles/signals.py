from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import VolunteerProfile, SponsorProfile, MemberProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'VOLUNTEER':
            VolunteerProfile.objects.create(user=instance)
        elif instance.user_type == 'SPONSOR':
            SponsorProfile.objects.create(user=instance)
        elif instance.user_type == 'MEMBER':
            MemberProfile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'VOLUNTEER':
        instance.volunteer_profile.save()
    elif instance.user_type == 'SPONSOR':
        instance.sponsor_profile.save()
    elif instance.user_type == 'MEMBER':
        instance.member_profile.save()
