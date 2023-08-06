from django.urls import path, include

from charityapp.work.views import CharityCampaignDetailsView, CharityCampaignsView, WhatWeDoView, WhereWeWork, \
    ParticipationThankYouView, DonationCampaignsView, DonationCampaignDetailsView, CharityCampaignParticipationView, \
    SponsorDonationView

urlpatterns = [
    path('charity-campaigns/', include([
        path('', CharityCampaignsView.as_view(), name='charity-campaigns'),
        path('<int:pk>/', CharityCampaignDetailsView.as_view(), name='charity-campaign-details'),
        path('participate/<int:campaign_id>/', CharityCampaignParticipationView.as_view(),
             name='charity-campaign-participation'),
        path('participate/thank-you/', ParticipationThankYouView.as_view(), name='participation-thank-you'),
    ])),
    path('donation-campaigns/', include([
        path('', DonationCampaignsView.as_view(), name='donation-campaigns'),
        path('<int:pk>/', DonationCampaignDetailsView.as_view(), name='donation-campaign-details'),
        path('donate/<int:campaign_id>/', SponsorDonationView.as_view(), name='sponsor-donation'),
        # path('participate/thank-you/', ParticipationThankYouView.as_view(), name='participation-thank-you-page'),
    ])),
    path('what-we-do/', WhatWeDoView.as_view(), name='what-we-do'),
    path('where-we-work/', WhereWeWork.as_view(), name='where-we-work'),
]
