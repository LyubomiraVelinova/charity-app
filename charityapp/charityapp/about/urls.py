from django.urls import path

from charityapp.about.views import WhoWeAreListView, MissionAndValuesView, HistoryView

urlpatterns = [
    path('', WhoWeAreListView.as_view(), name='who-we-are-page'),
    path('values/', MissionAndValuesView.as_view(), name='mission-and-values-page'),
    path('history/', HistoryView.as_view(), name='history-page'),
]
