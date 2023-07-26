from django.urls import path

from charityapp.about.views import mission_and_values, history, WhoWeAreListView

urlpatterns = [
    path('values/', mission_and_values, name='mission_and_values-page'),
    path('', WhoWeAreListView.as_view(), name='who-we-are-page'),
    path('history/', history, name='history-page'),
]