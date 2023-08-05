from django.contrib import admin

from charityapp.about.models import Person, Timeline


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'member_role', 'description']
    ordering = ['first_name']


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ['event_date', 'event_title', 'get_first_fifty_words']
    readonly_fields = ('get_first_fifty_words',)
    ordering = ['-event_date']


