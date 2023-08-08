from django.urls import path

from charityapp.contact.views import ContactUsView, ContactThankYouView

urlpatterns = [
    path('', ContactUsView.as_view(), name='contact-us'),
    path('thank-you/', ContactThankYouView.as_view(), name='contact-thank-you'),
]
