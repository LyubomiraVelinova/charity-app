from django.contrib import admin

from charityapp.charity.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['quote', 'date', 'author', 'approved']
    list_filter = ('approved',)
    actions = ['approve_selected']

    def approve_selected(self, request, queryset):
        queryset.update(approved=True)

    approve_selected.short_description = 'Approve selected testimonials'
