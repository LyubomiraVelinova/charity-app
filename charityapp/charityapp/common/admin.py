from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from charityapp.common.models import AboutUsInfo, RandomUserDonation, Impact, LatestNews


# from charityapp.common.models import AboutUsInfo
# from charityapp.user_profiles.models import Sponsor, Volunteer, Member

# UserModel = get_user_model()
#
#
# @admin.register(AboutUsInfo)
# class UserModelAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Info', {
#             'fields': ('header', 'description')
#         }),
#         ('Updated on', {
#             'fields': ('last_updated',)
#         }),
#     )


@admin.register(AboutUsInfo)
class AboutUsInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(RandomUserDonation)
class DonationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Donation Value', {
            'fields': ('donation_amount',)
        }),
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Billing Information', {
            'fields': ('country', 'city', 'postal_code', 'address')
        }),
        ('Payment Method', {
            'fields': (
                'payment_method',)
        }),
        ('Card Information', {
            'fields': (
                'holder_name', 'card_verification_value', 'card_number', 'card_expiration_month',
                'card_expiration_year')
        }),
    )
    list_display = ('get_full_name', 'email', 'phone_number', 'donation_amount')
    list_filter = ('donation_amount',)
    search_fields = ('first_name', 'last_name', 'email')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = 'Full Name'


@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    list_display = ['title', 'resume', 'achievement_numbers']
    search_fields = ('title',)

    # @staticmethod
    # def show_picture(self, obj):
    #     return mark_safe(f'<img src="/media/{obj.picture}" width = "150" height = "150" / > ')


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Event Content', {
            'fields': ('title', 'description')
        }),
        ('Event Date', {
            'fields': ('event_date',)
        }),
    )
    list_display = ['event_date', 'title', 'description']
    list_filter = ['event_date']
    ordering = ['-event_date']
