from django.contrib import admin

from charityapp.accounts.models import AppUser
from charityapp.user_profiles.models import SponsorProfile, VolunteerProfile, MemberProfile


# class AppUserAdmin(admin.TabularInline):
#     model = AppUser
#     extra = 1


@admin.register(SponsorProfile)
class SponsorProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'website', 'career_field']
    # inlines = ('AppUserAdmin',)
    search_fields = ('company_name', 'career_field')
    filter_horizontal = ('donation_history',)

    fieldsets = (
        ('Company Details', {
            'fields': ('company_name', 'logo', 'website', 'career_field')
        }),
        ('Donation History', {
            'fields': ('donation_history',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # Make the user field read-only for existing records
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        # Disable the delete permission for member profiles to prevent accidental deletions
        return False

    def has_add_permission(self, request):
        # Disable the add permission for member profiles to prevent duplicate records
        return False


@admin.register(VolunteerProfile)
class VolunteerProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'bio', 'phone_number', 'interests')
    list_filter = ('gender', 'interests')
    search_fields = ('first_name', 'last_name', 'interests')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'gender', 'profile_picture', 'phone_number', 'bio', 'interests')
        }),
        ('Volunteer History', {
            'fields': ('charity_history', 'donation_history')
        }),
    )

    readonly_fields = ('full_name',)

    def get_readonly_fields(self, request, obj=None):
        # Make the user field read-only for existing records
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        # Disable the delete permission for volunteer profiles to prevent accidental deletions
        return False

    def has_add_permission(self, request):
        # Disable the add permission for volunteer profiles to prevent duplicate records
        return False


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'phone_number', 'role', 'strengths', 'interests')
    list_filter = ('gender', 'role', 'strengths')
    search_fields = ('first_name', 'last_name', 'role')

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'first_name', 'last_name', 'gender', 'profile_picture', 'phone_number', 'strengths', 'interests',
                'role')
        }),
        ('Charity History', {
            'fields': ('charity_history',)
        }),
    )

    readonly_fields = ('full_name',)

    def get_readonly_fields(self, request, obj=None):
        # Make the user field read-only for existing records
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        # Disable the delete permission for member profiles to prevent accidental deletions
        return False

    def has_add_permission(self, request):
        # Disable the add permission for member profiles to prevent duplicate records
        return False
