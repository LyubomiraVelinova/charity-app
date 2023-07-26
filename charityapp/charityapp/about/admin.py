from django.contrib import admin

from charityapp.about.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'member_role', 'description']
    ordering = ['first_name']


