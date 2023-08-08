from django.urls import path, include

from charityapp.causes.views import CharityCausesView, CharityCauseDetailsView, CharityCauseParticipationView, \
    ParticipationThankYouView, DonationCausesView, DonationCauseDetailsView, SponsorDonationView

urlpatterns = [
    path('charity-campaigns/', include([
        path('', CharityCausesView.as_view(), name='charity-causes'),
        path('<int:pk>/', CharityCauseDetailsView.as_view(), name='charity-cause-details'),
        path('participate/<int:campaign_id>/', CharityCauseParticipationView.as_view(),
             name='charity-cause-participation'),
        path('participate/thank-you/', ParticipationThankYouView.as_view(), name='participation-thank-you'),
    ])),
    path('donation-campaigns/', include([
        path('', DonationCausesView.as_view(), name='donation-causes'),
        path('<int:pk>/', DonationCauseDetailsView.as_view(), name='donation-cause-details'),
        path('donate/<int:campaign_id>/', SponsorDonationView.as_view(), name='sponsor-donation'),
    ])),
]
