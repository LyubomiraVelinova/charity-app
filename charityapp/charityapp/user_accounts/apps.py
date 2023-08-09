from django.apps import AppConfig


class UserAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charityapp.user_accounts'

    # Way to register signals
    def ready(self):
        result = super().ready()
        return result
