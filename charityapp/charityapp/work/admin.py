from django.contrib import admin
from django.contrib.auth import get_user_model

from charityapp.work.models import CharityCampaigns, DonationCampaigns


@admin.register(CharityCampaigns)
class CharityCampaignsAdmin(admin.ModelAdmin):
    list_display = ['name', 'resume', 'type', 'duration']
    fieldsets = (
        ('Home-page Info', {
            'fields': ('name', 'resume', 'image')
        }),
        ('Learn more Info', {
            'fields': ('description', 'motivation', 'start_date', 'end_date', 'type', 'website')
        }),
    )
    # NOT WORKING???
    verbose_name = 'Charity campaigns lists'


@admin.register(DonationCampaigns)
class DonationCampaignsAdmin(admin.ModelAdmin):
    list_display = ['title', 'current_amount', 'goal_amount', 'start_date', 'end_date', 'succeeded']
    search_fields = ['title', 'succeeded']
    # NOT WORKING???
    verbose_name_plural = 'Donation campaigns lists'
