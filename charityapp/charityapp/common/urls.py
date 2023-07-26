from django.urls import path, include

from charityapp.common.views import index, DonationView, DonationThankYouView

urlpatterns = [
    path('', index, name='home-page'),
    path('donation/', include([
        path('', DonationView.as_view(), name='donation-page'),
        path('thank-you/', DonationThankYouView.as_view(), name='donation-thank-you-page'),
    ])
         ),
    # path('about/', AboutUsView.as_view(), name='about-us-page'),
    # path('work/', our_work, name='our-work-page'),
]
