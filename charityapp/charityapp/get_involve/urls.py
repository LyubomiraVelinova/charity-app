from django.urls import path, include

from charityapp.get_involve.views import ways_to_help, ContactUsView, ContactThankYouView, WaysToInvolve, BlogView

urlpatterns = [
    path('ways-to-involve/', WaysToInvolve.as_view(), name='ways-to-involve'),
    path('how-to-help/', ways_to_help, name='how-to-help'),
    path('contact/', include([
        path('', ContactUsView.as_view(), name='contact-us'),
        path('thank-you/', ContactThankYouView.as_view(), name='contact-thank-you'),
    ])
         ),
    path('blog/', BlogView.as_view(), name='blog-page')
]
