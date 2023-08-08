from django.urls import path

from charityapp.about.views import WhoWeAreListView, MissionAndValuesView, HistoryView, WhatWeDoView, WhereWeWorkView

urlpatterns = [
    path('', WhoWeAreListView.as_view(), name='who-we-are-page'),
    path('values/', MissionAndValuesView.as_view(), name='mission-and-values-page'),
    path('history/', HistoryView.as_view(), name='history-page'),
    path('what-we-do/', WhatWeDoView.as_view(), name='what-we-do-page'),
    path('where-we-work/', WhereWeWorkView.as_view(), name='where-we-work-page'),
]
