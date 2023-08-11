from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from charityapp.user_accounts.forms import RegisterUserForm

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
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    list_display = ("email", "user_type", "is_superuser", "is_staff", "last_login")
    list_filter = ("user_type",)

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as e:
            print("An error occurred during save:", str(e))
