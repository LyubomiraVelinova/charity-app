from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from charityapp.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class CustomUserAdmin(auth_admin.UserAdmin):
    fieldsets = [
        (None, {
            "fields": ("email", "password"),
            "description": "Needed info to login",
        }),
        ("Permissions", {
            "fields": (
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
    ]
    form = RegisterUserForm
    list_display = ("email", "is_staff", "is_superuser",)
    list_filter = ("is_staff", "is_superuser", "groups")
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(UserModel)
class AppUserAdmin(CustomUserAdmin):
    # form = RegisterUserForm
    pass
