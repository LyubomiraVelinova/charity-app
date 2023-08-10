from django.urls import path, include

from charityapp.common.views import index, DonationView, DonationThankYouView

urlpatterns = [
    path('', index, name='home-page'),
    path('donate/', include([
        path('', DonationView.as_view(), name='donation-page'),
        path('thank-you/', DonationThankYouView.as_view(), name='donation-thank-you-page'),
    ])),
]
