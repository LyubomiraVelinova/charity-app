from django.urls import path

from charityapp.get_involved.views import WaysToInvolve

urlpatterns = [
    path('ways-to-involve/', WaysToInvolve.as_view(), name='ways-to-involve'),
]
