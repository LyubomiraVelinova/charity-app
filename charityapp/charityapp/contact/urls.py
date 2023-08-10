from django.urls import path

from charityapp.contact.views import ContactView, ContactThankYouView

urlpatterns = [
    path('', ContactView.as_view(), name='contact-page'),
    path('thank-you/', ContactThankYouView.as_view(), name='contact-thank-you-page'),
]
