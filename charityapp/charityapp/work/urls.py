from django.urls import path, include

from charityapp.work.views import CampaignDetailsView, CampaignsView, WhatWeDoView, WhereWeWork, participate_campaign

urlpatterns = [
    path('campaign/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details-page'),
    path('campaigns/', CampaignsView.as_view(), name='campaigns-page'),
    path('campaigns/participate/<int:campaign_id>', participate_campaign, name='participate-campaign'),
    path('what-we-do/', WhatWeDoView.as_view(), name='what-we-do-page'),
    path('where-we-work/', WhereWeWork.as_view(), name='where-we-work-page'),
    # path('donation/', DonationListView.as_view(), name='donation-campaigns-page'),
]
