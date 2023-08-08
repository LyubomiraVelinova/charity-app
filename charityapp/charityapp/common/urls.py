from django.urls import path, include

from charityapp.common.views import index, DonationView, DonationThankYouView

urlpatterns = [
    path('', index, name='homepage'),
    path('donation/', include([
        path('', DonationView.as_view(), name='donation'),
        path('thank-you/', DonationThankYouView.as_view(), name='donation-thank-you'),
    ])
         ),
]
