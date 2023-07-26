from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charityapp.accounts'

    # # Way to register signals
    # def ready(self):
    #     import charityapp.accounts.signals
    #     result = super().ready()
    #     return result
