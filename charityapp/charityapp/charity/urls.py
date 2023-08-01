from django.urls import path

from charityapp.charity.views import testimonial_submission

urlpatterns = [
    path('testimonial-submit/', testimonial_submission, name='testimonial-submission-page')
]
