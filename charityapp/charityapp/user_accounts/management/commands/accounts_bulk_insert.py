from django.core.management.base import BaseCommand

from charityapp.user_accounts.models import AppUser


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        users_data = [
            {
                "email": "volunteer1@ex.com",
                "password": "Liubomira1",
                "is_staff": False,
                "user_type": "VOLUNTEER",
                "created_at": "2023-07-01",
            },
            {
                "email": "member1@ex.com",
                "password": "Liubomira1",
                "is_staff": True,
                "user_type": "MEMBER",
                "created_at": "2023-07-02",
            },
            {
                "email": "sponsor1@ex.com",
                "password": "Liubomira1",
                "is_staff": False,
                "user_type": "SPONSOR",
                "created_at": "2023-07-03",
            },
            {
                "email": "volunteer2@ex.com",
                "password": "Liubomira1",
                "is_staff": True,
                "user_type": "VOLUNTEER",
                "created_at": "2023-07-04",
            },
            {
                "email": "member2@ex.com",
                "password": "Liubomira1",
                "is_staff": False,
                "user_type": "MEMBER",
                "created_at": "2023-07-05",
            },
            {
                "email": "sponsor2@ex.com",
                "password": "Liubomira1",
                "is_staff": True,
                "user_type": "SPONSOR",
                "created_at": "2023-07-06",
            },
            {
                "email": "volunteer3@ex.com",
                "password": "Liubomira1",
                "is_staff": False,
                "user_type": "VOLUNTEER",
                "created_at": "2023-07-07",
            },
            {
                "email": "member3@ex.com",
                "password": "Liubomira1",
                "is_staff": True,
                "user_type": "MEMBER",
                "created_at": "2023-07-08",
            },
            {
                "email": "sponsor3@ex.com",
                "password": "Liubomira1",
                "is_staff": False,
                "user_type": "SPONSOR",
                "created_at": "2023-07-09",
            },
        ]

        accounts_instances = [AppUser(**data) for data in users_data]
        AppUser.objects.bulk_create(accounts_instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in user_accounts_appusers table.'))
