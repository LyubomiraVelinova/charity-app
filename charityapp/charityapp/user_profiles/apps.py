from django.apps import AppConfig


class UserProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charityapp.user_profiles'
    verbose_name = "User Profile App"

    def ready(self):
        result = super().ready()
        return result
