from django.urls import path, include

from charityapp.get_involve.views import volunteers, ways_to_help, ContactView, ContactThankYouView

urlpatterns = [
    path('volunteers/', volunteers, name='volunteers-page'),
    path('how-to-help/', ways_to_help, name='how-to-help-page'),
    path('contact/', include([
        path('', ContactView.as_view(), name='contact-us-page'),
        path('thank-you/', ContactThankYouView.as_view(), name='contact-thank-you-page'),
    ])
         )
]
