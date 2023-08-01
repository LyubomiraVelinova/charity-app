from django.contrib import admin

from charityapp.charity.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass
