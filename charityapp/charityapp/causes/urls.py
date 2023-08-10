from django.urls import path, include

from charityapp.causes.views import CharityCausesView, CharityCauseDetailsView, CharityCauseParticipationView, \
    CharityCauseParticipationThankYouView, DonationCausesView, DonationCauseDetailsView, DonationCauseParticipationView

urlpatterns = [
    path('charity/', include([
        path('', CharityCausesView.as_view(), name='charity-causes-page'),
        path('<int:pk>/', CharityCauseDetailsView.as_view(), name='charity-cause-details-page'),
        path('participation/', include([
            path('<int:campaign_id>/', CharityCauseParticipationView.as_view(), name='charity-cause-participation'),
            path('thank-you/', CharityCauseParticipationThankYouView.as_view(),
                 name='charity-cause-participation-thank-you-page'),
        ])),
    ])),
    path('donation/', include([
        path('', DonationCausesView.as_view(), name='donation-causes-page'),
        path('<int:pk>/', DonationCauseDetailsView.as_view(), name='donation-cause-details-page'),
        path('participation/<int:campaign_id>/', DonationCauseParticipationView.as_view(),
             name='donation-cause-participation'),
    ])),
]
