from django.urls import path

from charityapp.get_involved.views import GetInvolvedView

urlpatterns = [
    path('', GetInvolvedView.as_view(), name='get-involved-page'),
]
