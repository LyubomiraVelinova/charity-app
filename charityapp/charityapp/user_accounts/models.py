from enum import Enum

from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone

from charityapp.common.mixins import ChoicesStringsMixin


class UserType(ChoicesStringsMixin, Enum):
    SPONSOR = "SPONSOR"
    VOLUNTEER = "VOLUNTEER"
    MEMBER = "MEMBER"


class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = "email"
    objects = AppUserManager()
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    user_type = models.CharField(
        max_length=UserType.max_length(),
        choices=UserType.choices(),
        null=False,
        blank=False,
    )
    created_at = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            # This is a new instance, set the created_at field with the current date and time
            self.created_at = timezone.now().date()
        super().save(*args, **kwargs)