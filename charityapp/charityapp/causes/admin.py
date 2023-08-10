from django.contrib import admin

from charityapp.causes.models import CharityCause, DonationCause, FAQ


@admin.register(CharityCause)
class CharityCauseAdmin(admin.ModelAdmin):
    list_display = ['name', 'resume', 'type', 'duration']
    fieldsets = (
        ('Home-page Info', {
            'fields': ('name', 'resume', 'image')
        }),
        ('Learn more Info', {
            'fields': ('description', 'motivation', 'start_datetime', 'end_datetime', 'type', 'website')
        }),
    )


@admin.register(DonationCause)
class DonationCauseAdmin(admin.ModelAdmin):
    list_display = ['title', 'current_amount', 'goal_amount', 'start_date', 'end_date', 'succeeded']
    search_fields = ['title', 'succeeded']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'important')
    search_fields = ('question',)

    fieldsets = (
        ('Question and Answer', {
            'fields': ('question', 'answer')
        }),
        ('Important Note', {
            'fields': ('important',)
        }),
        ('Related Campaigns', {
            'fields': ('campaigns',)
        }),
    )

    filter_horizontal = ('campaigns',)  # Display the campaigns field as a horizontal filter

    readonly_fields = ('question',)  # Make the question field read-only in the admin form
